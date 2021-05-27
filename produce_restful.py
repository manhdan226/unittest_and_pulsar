from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from decimal import Decimal
import json
from security import authenticate, identity
import pulsar
import boto3 


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)
def receive_message(request_data):
	new_data = {
				"id" : request_data["id"],
				"message": request_data["message"],
				"create_at": request_data["create_at"],
				"package": request_data["package"]
			}
	return new_data

class Tracking(Resource):
	#@jwt_required()
	def post(self):
		request_data = request.get_json()
		new_data = receive_message(request_data)
		
		print(new_data)
		#new_data = json.loads((new_data), parse_float=Decimal)
		encode_new_data = json.dumps(new_data, indent=2).encode('utf-8')
		
		client = pulsar.Client('pulsar://localhost:6650')
		producer = client.create_producer('pulsar-test')
		producer.send(encode_new_data)
		client.close()

		return new_data

api.add_resource(Tracking, '/tracking')

if __name__ == '__main__':
	app.run(port = 6550)