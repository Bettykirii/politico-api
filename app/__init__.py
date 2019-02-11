from flask import Flask

from instance.config import app_config

def create_app(config_name):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_object(app_config[config_mode])
  app.config.from_pyfile('config.py')
  from app.v1.views import party_view,office_view
  app.register_blueprint(party_view.b_v1,office_view.b_v1)
  return app   
   
    