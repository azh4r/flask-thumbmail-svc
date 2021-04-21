from flask import Flask, render_template
import logging
from flask_restful import Api
from .resources import add_resource

logger = logging.getLogger(__name__)


app = Flask(__name__)
api = Api(app)
add_resource(api)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")