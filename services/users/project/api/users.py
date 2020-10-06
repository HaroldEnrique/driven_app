# services/users/project/api/users.py

from flask import Blueprint
from flask_restful import Resource, Api

from project import db
from project.api.models import User

users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)


class UsersPing(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'pong!'
    }

api.add_resource(UsersPing, '/users/ping')
