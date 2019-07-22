"""
These are the global Objects, that are needed by the
  Controllers
  Models
"""
from flask import Flask
from flask_restplus import Api


def create_app():
    app = Flask(__name__)
    return app


def create_api(app):
    api = Api(app)
    return api


APP = create_app()
API = create_api(APP)
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Needed is SQL-Alchemy project
# Enable or disable the mask field, by default X-Fields
APP.config['RESTPLUS_MASK_SWAGGER'] = False
VERSION = "1"
"""
ns_conf controls the root of the URL  - plus the Version
"""
NS_CONF = API.namespace('tim' + VERSION, description=' dependencies')