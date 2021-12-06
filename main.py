from flask import Flask,request
from flask_restful import Api,Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app) # wrapping up
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # to name the db database.db
db = SQLAlchemy(app) # wrapping up

class PeepModel(db.Model):
	fname = db.Column(db.String(50),primary_key=True)
	surname = db.Column(db.String(50),primary_key=True)
	age = db.Column(db.Integer,nullable=False)

	def __repr__(self):
		return f'(name={name},surname={surname},age={age})' # data representation

# db.create_all() # delete/comment out after you're done

peep_put_args = reqparse.RequestParser()	# args for object
# peep_put_args.add_argument('fname',default=False,type=str,help='Peep\'s firstname',required=True)
peep_put_args.add_argument('surname',default=False,type=str,help='Peep\'s surname',required=True)
peep_put_args.add_argument('age',type=int,help='Peep\'s Age',required=True)	# adding an arg & its specs

resource_fields = {
	'fname': db.String,
	'surname': db.String,
	'age': db.Integer
}

class HelloWorld(Resource):
	@marshal_with(resource_fields)
	def get(self,name):
		result = PeepModel.query.get(fname=name)
		return result

	def put(self,name):
		cancel_put_request(name)
		my_attrs = peep_put_args.parse_args()	# it takes the ff. peep_put_args's arg reqs
		peep[name] = my_attrs	# adding objects
		return peep[name],201	# add http status code for the changes you did

	def delete(self,name):
		cancel_get_request(name)
		del peep[name]
		return '',204	# Leave the message blank

# Registering it in our api, just like the django urls
api.add_resource(HelloWorld, '/helloworld/<string:name>')

if __name__ == '__main__':
	app.run(debug=True)