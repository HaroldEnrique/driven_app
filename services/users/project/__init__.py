# services/users/project/__init__.py

import os
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy  # nuevo

# instanciando la app
app = Flask(__name__)

api = Api(app)

# establecer configuración
#app.config.from_object("project.config.DevelopmentConfig")  # nuevo

# estableciendo config
app_settings = os.getenv('APP_SETTINGS')  # nuevo
app.config.from_object(app_settings)      # nuevo

# instanciado la db
db = SQLAlchemy(app)  # nuevo

# modelo

class User(db.Model):  # nuevo
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


class UsersPing(Resource):
    def get(self):
        return {"status": "success", "menssage": "pong!"}

api.add_resource(UsersPing, "/users/ping")
