from flask import Flask, jsonify, render_template
from flask_smorest import Api
from db import db

import os

from resources.outlook_login import blp as LoginBlueprint
from resources.student import student_blp
from resources.enroller import enroller_blp
from resources.meeting_link import meeting_link_blp

def create_app(db_url=None):
    app = Flask(__name__)

    #we need app in the JWTManager(app) to create the endpoint

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dbpass1234@34.230.58.127/eece-queue-db'
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "EECE_Queuing_System"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app) #this is the same as db = SQLAlchemy(app)


    api = Api(app) 

    api.register_blueprint(LoginBlueprint, url_prefix="/login")
    api.register_blueprint(student_blp)
    api.register_blueprint(enroller_blp)
    api.register_blueprint(meeting_link_blp)

    return app