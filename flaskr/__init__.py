
import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .display import display
    
    app.register_blueprint(display, url_prefix='/')


    return app