from flask import Flask

app = Flask(__name__, static_folder='static')

app.config.from_pyfile('config.py')

from app.mod_routing.controllers import mod_routing as routing_module

app.register_blueprint(routing_module)
