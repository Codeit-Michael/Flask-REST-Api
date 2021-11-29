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
peep_put_args.add_argument('name',type=str,help='Peep\'s Name')	# adding an arg & its specs
peep_put_args.add_argument('age',type=int,help='Peep\'s Age')
peep_put_args.add_argument('married',type=bool,help='Peep\'s Marital status')

peep = {}

class HelloWorld(Resource):
	def get(self,name):
		return(peep[name])

	def put(self,name):
		my_args = peep_put_args.parse_args()
		return my_args

# Registering it in our api, just like the django urls
api.add_resource(HelloWorld, '/helloworld/<string:name>')

if __name__ == '__main__':
	app.run(debug=True)