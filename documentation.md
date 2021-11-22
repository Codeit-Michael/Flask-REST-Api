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


4. Making simple Hello world
	@app.route("/")
	def hello_world():
		return "<p>Hello, World!</p>"


5. Returning a JSON
-You can return a JSON even you don't have a db by the ff., consider getting on that route:
	db = {
		"12": {
				"task": "wash dishes"
		},
		"13": {
			"task": "something else"
		}
	}

	@app.route('/get-todos')
	def getTodos():
		return db

6. Returning Hello world using our Api
	class HelloWorld(resource):
		def get(self):
			return {'message': 'hello world'}	# JSONs should be serializable

	api.add_resource(HelloWorld, '/')	# Registering it in our api, just like the django urls

-Next is create a test.py file for testing our api:
	import requests

	BASE = "http//127.0.0.1:5000/"		# getting the base / main home of our localhost
	
	response = requests.get(BASE + '')	# declaring to get the action, with home & extra link
	print(response.json())				# calling it

-After it, run the two pyfiles; the main.py and the test.py:
	-you will see, our test.py wwill get what it want.