# src/api/ping.py

#created a new instance of the blueprint class and bounded the ping
#resource thru it
from flask import Blueprint
from flask_restx import Resource, Api

ping_namespace = Namespace('ping')
#ping_blueprint = Blueprint('ping', __name__)
#api = Api(ping_blueprint)


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


#api.add_resource(Ping, '/ping')
ping_namespace.add_resource(Ping, "")