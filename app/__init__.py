from flask import Flask
import psycopg2
from app.v1.views.office_view import b_v1
from app.v1.views.party_view import b
# from app.v2.views.views_user_signup import b
from instance.config import app_config

def create_app(config_name):

    app = Flask(__name__)

     # Creating the app configurations
    # app.config.from_object(app_config[config_name])

    #Registering the blueprint
    app.register_blueprint(b_v1)
    app.register_blueprint(b)
#     app.register_blueprint(v2)
    return app