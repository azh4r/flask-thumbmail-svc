from flask import Flask, render_template
import logging
from flask_restful import Api
from .resources import add_resource
import os

logger = logging.getLogger(__name__)

def create_app(test_config=None):
    app = Flask(__name__)
    if test_config == None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        #load the test_config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # create flask_restful app
    api = Api(app)
    add_resource(api)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

