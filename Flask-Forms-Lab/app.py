from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

username = "yasmina"
password = "12345"
facebook_friends=["leen","bean","finly", "frankly", "giries", "jamal"]


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
	return render_template('home.html',facebook_friends=facebook_friends)






if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)