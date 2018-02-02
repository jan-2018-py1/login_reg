from myconnection import MySQLConnector
from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "My secret session key"
mysql = MySQLConnector(app, "login_reg_jan_2018")
import re
Email_key = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

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
	dataIsValid = True
# First Name - letters only, at least 2 characters and that it was submitted

	if not first_name.isalpha() or len(first_name) < 2:
		flash("First name must be at least 2 and alphabetical")
		dataIsValid = False
	if not last_name.isalpha() or len(last_name) < 2:
		flash("Last name must be at least 2 and alphabetical")
		dataIsValid = False
	if not Email_key.match(email):
		flash("Email not valid")
		dataIsValid = False
	if len(password) < 8 or password != confirm:
		flash("Password must be at least 8 and match confirm")
		dataIsValid = False

	if dataIsValid:
		query = "INSERT INTO `users` (`first_name`, `last_name`, `email`, `password`) VALUES (:spot_one, :spot_two, :spot_three, :spot_four);"
		data = {
			"spot_one":first_name,
			"spot_two":last_name,
			"spot_three":email,
			"spot_four":password,
		}
		myVar = mysql.query_db(query, data)
		session["user_id"] = myVar
		return redirect("/dashboard")
	else:
		return redirect("/")
@app.route("/dashboard")
def dashboard():
	query = "SELECT * FROM users WHERE id = :user_id"
	data = {
		"user_id":session["user_id"]
	}
	user = mysql.query_db(query, data)[0] # list of dictionaries, take the first index
	return render_template("dashboard.html", user=user)

@app.route("/login", methods=["POST"])
def login():
	query = "SELECT * FROM users WHERE email = :email"
	data = {
		"email":request.form["email"]
	}
	user = mysql.query_db(query, data) # LIST [],  [{}]
	#check if user is there
	if user:
		user = user[0]
		#check if password matches
		if user["password"] == request.form["password"]:
			#logg user in
			session["user_id"] = user["id"]
			return redirect("/dashboard")
	flash("no email and password combo found")
	return redirect("/")
@app.route("/logout")
def logout():
	session.clear()
	return redirect("/")
# Last Name - letters only, at least 2 characters and that it was submitted
# Email - Valid Email format, and that it was submitted
# Password - at least 8 characters, and that it was submitted
# Password Confirmation - matches password

app.run(debug=True)