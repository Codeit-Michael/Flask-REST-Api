from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
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
		return f'Peep(id={id},name={name},age={age})' # data representation

# db.create_all() # delete/comment out after you're done

peep_put_args = reqparse.RequestParser()	# args for object
peep_put_args.add_argument('name',default=False,type=str,help='Peep\'s name',required=True)
peep_put_args.add_argument('age',type=int,help='Peep\'s Age',required=True)	# adding an arg & its specs

peep_patch_args = reqparse.RequestParser()
peep_patch_args.add_argument('name',default=False,type=str,help='Peep\'s name')
peep_patch_args.add_argument('age',type=int,help='Peep\'s Age')

resource_fields = {
	'id': fields.Integer, 
	'name': fields.String,
	'age': fields.Integer
}

class HelloWorld(Resource):
	@marshal_with(resource_fields)
	def get(self,peep_id):
		result = PeepModel.query.filter_by(id=peep_id).first()
		if not result:
			abort(404, message="Could not find video with that id")
		return result

	@marshal_with(resource_fields)
	def put(self,peep_id):
		args = peep_put_args.parse_args()	# it takes the ff. peep_put_args's arg reqs
		if PeepModel.query.filter_by(id=peep_id).first():
		# if result:
			abort(409,message=f'ID {peep_id} already taken...')
		peep = PeepModel(id=peep_id,name=args['name'],age=args['age'])
		db.session.add(peep)
		db.session.commit()
		return peep,201	# add http status code for the changes you did

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

	def delete(self,peep_id):
		cancel_get_request(peep_id)
		del peep[peep_id]
		return '',204	# Leave the message blank

# Registering it in our api, just like the django urls
api.add_resource(HelloWorld, '/helloworld/<int:peep_id>')

if __name__ == '__main__':
	app.run(debug=True)