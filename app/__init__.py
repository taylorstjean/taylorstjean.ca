from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

from app.mod_routing.controllers import mod_routing as routing_module

app.register_blueprint(routing_module)
