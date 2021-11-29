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
			return {'message': 'hello world'}	# objects should be serializable (in JSON format)

	api.add_resource(HelloWorld, '/')	# Registering it in our api, just like the django urls

-Next is create a test.py file for testing our api:
	import requests

	BASE = "http//127.0.0.1:5000/"		# getting the base / main home of our localhost
	
	response = requests.get(BASE + '')	# declaring to get the action, with home & extra link
	print(response.json())				# calling it

-After it, run the two pyfiles; the main.py and the test.py:
	-you will see, our test.py wwill get what it want.
-You can also use other request methods such as post or delete, just make sure you had a 
function for that type of request method. To access other functions, replace/put the "get" 
method in response = requests.get(BASE + 'helloworld') to another name of function.


7. Putting parameters on our Api
-Modify the get() and add some parameter:
	def get(self,name,score):
		return {'name': name, 'score': score}

	-Replace api.add_resource(HelloWorld, '/helloworld') into:
	api.add_resource(HelloWorld, '/helloworld/<string:name>/<int:score>')

-Now lets add some name and int on the link we got on test.py:
	response = requests.get(BASE + 'helloworld/agg/3')

-If we try to run our test.py, it will get the name agg and the int 3 as its parameter


8. Storing data through Api
-Lets add requests on our api. Lets say on our test.py, where our actions are in, has 
parameters. Take note; to put some argument on our request file test.py, simply:
	response = requests.put(BASE + 'helloworld/Michael',{'subs': 1000})	# requests = argument

-To access the request/arguments inside the engine, we need to use the 'request' from the 
flask module. So import it: from flask import Flask,request

-In order to get the requests, we are going to use the put() to get the json we sent. To see 
if our Api works, try adding the ff. on your HelloWorld()/main.py:
	def put(self,name):
		print(request.form['subs'])
		return {}

-Then modify our route in test.py:
	response = requests.put(BASE + 'helloworld/Michael',{'subs': 1000})

-If you run our server and request file, your terminal for server will print the json we put.


9. Request Parser (reqparse)
-reqparse - built-in flask_restful function for request parsing, from the name itself. Just 
import it in flask_restful: from flask_restful import Api,Resource, reqparse

-reqparse.RequestParser() - allows us to parse trhough the data as long as the requirements 
of the object/JSON is satisfied

-Lets say we had a simple dictionary which simulates the db
	peep_put_args = reqparse.RequestParser()

-To add an argument and its specs:
	peep_put_args.add_argument('name',type=str,help='Peep Name') # adding an arg & its specs

-The sequence for add_argument() kwargs are; key,type,help='like an error message'

-If we send incopmplete args, this might happen:{'name': None, 'married': None}