from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self):
		return {'message': 'hello world'}

api.add_resource(HelloWorld, '/helloworld')	# Registering it in our api, just like the django urls

if __name__ == '__main__':
	app.run(debug=True)