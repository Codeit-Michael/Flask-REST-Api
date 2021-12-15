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
-You can also use other request methods such as post or delete, just make sure you had a function for that type of request method. To access other functions, replace/put the "get" method in response = requests.get(BASE + 'helloworld') to another name of function.


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
-Lets add requests on our api. Lets say on our test.py, where our actions are in, has parameters. Take note; to put some argument on our request file test.py, simply:
	response = requests.put(BASE + 'helloworld/Michael',{'subs': 1000})	# requests = argument

-To access the request/arguments inside the engine, we need to use the 'request' from the flask module. So import it: from flask import Flask,request

-In order to get the requests, we are going to use the put() to get the json we sent. To see if our Api works, try adding the ff. on your HelloWorld()/main.py:
	def put(self,name):
		print(request.form['subs'])
		return {}

-Then modify our route in test.py:
	response = requests.put(BASE + 'helloworld/Michael',{'subs': 1000})

-If you run our server and request file, your terminal for server will print the json we put.


9. Request Parser (reqparse)
-reqparse - built-in flask_restful function for request parsing, from the name itself. Just import it in flask_restful: from flask_restful import Api,Resource, reqparse

-reqparse.RequestParser() - allows us to parse trhough the data as long as the requirements of the object/JSON is satisfied

-Lets say we had a simple dictionary which simulates the db
	peep_put_args = reqparse.RequestParser()

-To add an argument and its specs:
	peep_put_args.add_argument('name',type=str,help='Peep Name') # adding an arg & its specs

-The sequence for add_argument() kwargs are; key,type,help='like an error message'

-If we send incopmplete args, this might happen:{'name': None, 'married': None}

-Taking and loading the args to work with it using:
	def put(self,name):
		my_args = peep_put_args.parse_args()	# it takes the following arg reqs
		return {name: my_args}

-If you run it with incomplete data, it won't crash because we didn't set it to be required unless we did, just add required=True in our chosen add_argument:
	peep_put_args.add_argument('age',type=int,help='Peep\'s Age',required=True)
	# if we didn't meet the requirement it, will crash and the message will pop on the screen

-Adding objects on db (for now, let's just use the dictionary as db which is named 'peep'). Let's also add http status code for actions we did. For now, let's add 201 because it means created:
	def put(self,name):
		my_attrs = peep_put_args.parse_args()	# it takes the ff. peep_put_args's arg reqs
		peep[name] = my_attrs	# adding objects
		return peep[name], 201	# add http status code for the changes you did


10. Validating requests
-If the name (the key object) is not in db/dict, we can abort finding an object with that key, we can avoid getting errors by retutrning abort():
	def cancel_request(name):
		if name not in peep:
			abort(404,message='Peep name could not found...')

-This is useful when you're using get(), and you can use this function in our get() or move the code

-As you can see, all of the posibilites we create we put http status code or else we will get an error.

-We can also do reverse in put() if the name already exists by adding;
	if name in peep: and then the condition


11. Making Delete()
	def delete(self,name):
		cancel_get_request(name)
		del peep[name]
		return '',204	# Leave the message blank


12. Installing database dependancy
-On command line/terminal: pip3 install flask_sqlalchemy


13. Db Configuration
-Import first the module we installed: from flask_sqlalchemy import SQLAlchemy

-Next at the bottom part of api wrapping config, add:
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # to name the db database.db
	db = SQLAlchemy(app) # wrapping up

-Let's say we want to store the db inside a folder called 'tmp', edit app.config and add 'tmp/' on the dir:
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/database.db'

-To initialize the db, run:
	db.create_all()
-Run this code once because it may overwrite your whole db if you did twice or more. 

-Before initializing the db, let's add models first, where we store objects (peep)


14. Creating a model
<!-- 
 	class PeepModel(db.Model):
		name = db.Column(db.String(50),primary_key=True)
		surname = db.Column(db.String(50),primary_key=True)
		age = db.Column(db.Integer,nullable=False)

		def __repr__(self):
			return f'(name={name},surname={surname},age={age})' # data representation

	db.create_all()
 -->

-And now you were ready to configure our db. To do that, just run your py file and once you're done, delete the line 'db.create_all()' or it will override your db next time.


15. Data Querying and serializing objects (to be readable as JSON)
-Edit our code get() for querying to the db:
	def get(self,name):
		result = PeepModel.query.get(fname=name)
		return result

-Now what it will return is an instance and not a JSON because remember what we add on our PeepModel; the repr(). So what we will do now is to serialize the instance it return into objects. Let's start by importing 'fields' and 'marshal_with' from flask restful so our import from this module are:
	from flask_restful import Api,Resource,reqparse,abort,fields,marshal_with

-Next is to add 'resource_fields'. It is the reference of data/objects we broke down to be a JSON, so add:
	resource_fields = {
		'fname': db.String,
		'surname': db.String,
		'age': db.Integer
	}

-To apply the resource_fields object ditrib classification when were querying data on db, at the top of our get() in HelloWorld, type:
	@marshal_with(resource_fields)

-So our get() in class HelloWorld looks like this:
		@marshal_with(resource_fields)
		def get(self,name):
			result = PeepModel.query.filter_by(fname=name).first()
			return result
			
-The filter_by() used it filters all the object with that attribute and first() used to return the first/main object it has.


16. Update objects
-We update an object through patch(). First, let's make its own args which is not required with all fields so we can just update what object field we want to update:
	peep_patch_args = reqparse.RequestParser()
	peep_patch_args.add_argument('name',default=False,type=str,help='Peep\'s name')
	peep_patch_args.add_argument('age',type=int,help='Peep\'s Age')

-Next, let's add the patch() on our HelloWorld():
	@marshal_with(resource_fields)
	def patch(self,peep_id):
		args = peep_patch_args.parse_args()
		result = PeepModel.query.filter_by(id=peep_id).first()
		if not result:
			abort(404, message="Peep doesn't exist, cannot update")
		if args['name']:
			result.name = args['name']
		if args['age']:
			result.views = args['age']
		db.session.commit()
		return result

-Now as we see here, we just .commit() it and not .add() because in flask rest, once an object is in db, you don't need to .add() it again and just commit it.