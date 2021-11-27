from flask import Flask,request
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

peep = {
	'Michael': {'age': 18, 'student': True},
	'Tim': {'age': 25, 'student': False},
}

vids = {}

@app.route('/')
def getTodos():
	return(peep)

class HelloWorld(Resource):
	def get(self,name):
		return(peep[name])

	def put(self,name):
		print(request.form['subs'])
		return {}

# Registering it in our api, just like the django urls
api.add_resource(HelloWorld, '/helloworld/<string:name>')

if __name__ == '__main__':
	app.run(debug=True)