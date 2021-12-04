from flask import Flask,request
from flask_restful import Api,Resource, reqparse

app = Flask(__name__)
api = Api(app)

# peep = {
# 	'Michael': {'age': 18, 'student': True},
# 	'Tim': {'age': 25, 'student': False},
# }

# peep = {}

# @app.route('/')
# def getTodos():
# 	return(peep)

peep_put_args = reqparse.RequestParser()						# args for object
peep_put_args.add_argument('age',type=int,help='Peep\'s Age',required=True)	# adding an arg & its specs
peep_put_args.add_argument('greet',default=False,type=str,help='Peep\'s greet',required=True)

peep = {}

class HelloWorld(Resource):
	def get(self,name):
		return {name:peep[name]}

	def put(self,name):
		my_attrs = peep_put_args.parse_args()	# it takes the ff. peep_put_args's arg reqs
		peep[name] = my_attrs	# adding objects
		return peep[name], 201	# add http status code for the changes you did

# Registering it in our api, just like the django urls
api.add_resource(HelloWorld, '/helloworld/<string:name>')

if __name__ == '__main__':
	app.run(debug=True)