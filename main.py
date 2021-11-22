from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self,name,score):
		return {'name': name, 'score': score}

# Registering it in our api, just like the django urls
api.add_resource(HelloWorld, '/helloworld/<string:name>/<int:score>')

if __name__ == '__main__':
	app.run(debug=True)