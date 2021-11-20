from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

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


if __name__ == '__main__':
	app.run(debug=True)