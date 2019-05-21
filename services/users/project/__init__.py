from flask import Flask, jsonify
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)

# Set the config
app.config.from_object('project.config.DevelopmentConfig')


class UserPing(Resource):
    """
    Test User Api
    """
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!',
        }


api.add_resource(UserPing, '/users/ping')
