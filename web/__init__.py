from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    
    from . import drawing
    app.register_blueprint(drawing.bp)



    return app
