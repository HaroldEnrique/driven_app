# services/users/project/__init__.py

import os
from flask import Flask
# from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy  # nuevo
from flask_debugtoolbar import DebugToolbarExtension  # nuevo

# instantiate the db
db = SQLAlchemy()
toolbar = DebugToolbarExtension()  # nuevo


def create_app(script_info=None):

    # instanciado la  app
    app = Flask(__name__)
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # configurar la extension
    db.init_app(app)
    toolbar.init_app(app)  # nuevo

    # registrar blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # contexto shell para flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app

# instanciando la app
# app = Flask(__name__)

# api = Api(app)

# establecer configuración
# app.config.from_object("project.config.DevelopmentConfig")  # nuevo

# estableciendo config
