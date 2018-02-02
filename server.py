from myconnection import MySQLConnector
from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "My secret session key"
mysql = MySQLConnector(app, "login_reg_jan_2018")
import re
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")


@app.route("/")
def index():
	if "user_id" in session:
		return redirect("/dashboard")
	return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
	print request.form
	first_name = request.form["first_name"]
	last_name = request.form["last_name"]
	email = request.form["email"]
	password = request.form["password"]
	confirm = request.form["confirm"]
	isValid = True
	if len(first_name) < 2 or not first_name.isalpha():
		flash("First name must be at least 2 characters and alphabetical")
		isValid = False

	if len(last_name) < 2 or not last_name.isalpha():
		flash("Last name must be at least 2 characters and alphabetical")
		isValid = False

	if not EMAIL_REGEX.match(email):
		flash("not a valid email format")
		isValid = False

	if len(password) < 8 or password != confirm:
		flash("password must be 8 and must match password confirm")
		isValid = False

	if isValid:
		query = "INSERT INTO `users` (`first_name`, `last_name`, `email`, `password`) VALUES (:one, :two, :three, :four);"
		data = {
			"one":first_name,
			"two":last_name,
			"three":email,
			"four":password
		}
		x = mysql.query_db(query, data)
		session["user_id"] = x
		return redirect("/dashboard")
	else:
		return redirect("/")
@app.route("/dashboard")
def dashboard():
	query = "SELECT * FROM users WHERE id = :user_id"
	data = {
		"user_id":session["user_id"]
	}
	user = mysql.query_db(query, data) #list of dictionaries
	return render_template("dashboard.html", user = user[0])

@app.route("/login", methods=["POST"])
def login():
	query = "SELECT * FROM users WHERE email = :post_email"
	data = {
		"post_email":request.form["email"]
	}
	user = mysql.query_db(query, data) # []
	print user
	if len(user) > 0:
		user = user[0]
		if user["password"] == request.form["password"]:
			session["user_id"] = user["id"]
			return redirect("/dashboard")
	flash("Email and password not found")
	return redirect("/")
	# 	else:
	# 		flash("Incorrect Password")
	# 		return redirect("/")
	# else:
	# 	flash("No email found")
	# 	return redirect("/")
@app.route("/logout")
def logout():
	session.clear()
	return redirect("/")
# First Name - letters only, at least 2 characters and that it was submitted
# Last Name - letters only, at least 2 characters and that it was submitted
# Email - Valid Email format, and that it was submitted
# Password - at least 8 characters, and that it was submitted
# Password Confirmation - matches password

app.run(debug=True)