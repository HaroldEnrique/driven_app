# services/users/project/__init__.py

import os
from flask import Flask, jsonify
from flask_restful import Resource, Api

# instanciando la app
app = Flask(__name__)

api = Api(app)

# establecer configuración
#app.config.from_object("project.config.DevelopmentConfig")  # nuevo

# estableciendo config
app_settings = os.getenv('APP_SETTINGS')  # nuevo
app.config.from_object(app_settings)      # nuevo

class UsersPing(Resource):
    def get(self):
        return {"status": "success", "menssage": "pong!"}

api.add_resource(UsersPing, "/users/ping")
