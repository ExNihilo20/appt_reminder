# serves double duty
# 1. contains the flask application factory
# 2. tells Python flaskr directory should be treated as a package

import os
import flaskr.db as db
from flask import Flask
from flaskr.utils.logging import info

info("general test")
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=db.build_connection_string(), 
        )
    info("database connection string grabbed")
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
