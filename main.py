from flask import Flask,request
from flask_restful import Api,Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app) # wrapping up
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # to name the db database.db
db = SQLAlchemy(app) # wrapping up

class PeepModel(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(50),nullable=True)
	age = db.Column(db.Integer,nullable=False)

	def __repr__(self):
		return f'(name={name},surname={surname},age={age})' # data representation

# db.create_all() # delete/comment out after you're done

peep_put_args = reqparse.RequestParser()	# args for object
# peep_put_args.add_argument('fname',default=False,type=str,help='Peep\'s firstname',required=True)
peep_put_args.add_argument('name',default=False,type=str,help='Peep\'s surname',required=True)
peep_put_args.add_argument('age',type=int,help='Peep\'s Age',required=True)	# adding an arg & its specs

resource_fields = {
	'id': db.Integer, 
	'name': db.String,
	'age': db.Integer
}
"""
REWRITE EVERYTHING!!!
"""

class HelloWorld(Resource):
	@marshal_with(resource_fields)
	def get(self,peep_id):
		result = PeepModel.query.filter_by(id=peep_id).first()
		return result

	@marshal_with(resource_fields)
	def put(self,peep_id):
		my_attrs = peep_put_args.parse_args()	# it takes the ff. peep_put_args's arg reqs
		result = PeepModel.query.filter_by(id=peep_id).first()
		if result:
			abort(409,f'User {name} already taken...')
		peep = PeepModel(id=peep_id,name=my_attrs['name'],age=my_attrs['age'])
		db.session.add(peep)
		db.session.commit()
		print('bobo')
		return peep,201	# add http status code for the changes you did

	def delete(self,peep_id):
		cancel_get_request(peep_id)
		del peep[name]
		return '',204	# Leave the message blank

# Registering it in our api, just like the django urls
api.add_resource(HelloWorld, '/helloworld/<int:peep_id>')

if __name__ == '__main__':
	app.run(debug=True)