from myconnection import MySQLConnector
from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "My secret session key"
mysql = MySQLConnector(app, "login_reg_jan_2018")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
	print request.form
# First Name - letters only, at least 2 characters and that it was submitted
# Last Name - letters only, at least 2 characters and that it was submitted
# Email - Valid Email format, and that it was submitted
# Password - at least 8 characters, and that it was submitted
# Password Confirmation - matches password

app.run(debug=True)