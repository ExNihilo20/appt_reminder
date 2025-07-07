# serves double duty
# 1. contains the flask application factory
# 2. tells Python flaskr directory should be treated as a package

import os
import flaskr.db as db
from flask import Flask



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
        DATABASE=
    )