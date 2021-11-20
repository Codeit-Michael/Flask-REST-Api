## MAKING REST API WITH FLASK ##

Note: Make sure you installed the ff. requirements
	-aniso8601
	-click
	-Flask
	-Flask-RESTful
	-Flask-SQLAlchemy
	-itsdangerous
	-Jinja2
	-MarkupSafe
	-pytz
	-six
	-SQLAlchemy
	-Werkzeug

# Starting an App
1. Make sure you import our 2 main modules to use:
	from flask import Flask
	from flask_restful import Api,Resource

2. Make you app
	app = Flask(__name__)
	api = Api(app)

	if __name__ == '__main__':
		app.run(debug=True)		# to show the debugger

3. Try running your app
	python3 main.py		# py filename

