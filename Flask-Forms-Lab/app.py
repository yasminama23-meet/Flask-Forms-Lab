from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	_name_,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

username = "yasmina"
password = "12345"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/')  # '/' for the default page
def login():
	if request.method == 'POST':
		if username == request.form['username'] and password == request.form['password']:
			return redirect(url_for('Home'))
		else:
			return render_template('login.html')
	return render_template('login.html')

@app.route('/home')
def Home():
	return render_template('home.html')






if _name_ == "_main_":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)