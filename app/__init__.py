from flask import Flask
from app.v1.views.office_view import b_v1
from instance.config import app_config

def create_app(config_name):

    app = Flask(__name__)

     # Creating the app configurations
    # app.config.from_object(app_config[config_name])

    #Registering the blueprint
    app.register_blueprint(b_v1)
    return app