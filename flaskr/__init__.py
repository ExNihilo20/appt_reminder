# serves double duty
# 1. contains the flask application factory
# 2. tells Python flaskr directory should be treated as a package

import os
from flask import Flask
from flaskr.utils.logging import info, debug

def create_app(test_config=None):
    debug("start...create_app")
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    debug(f"flask app name: {app}")
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        )
    info("app configured with: secret key,  database information")
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
        debug("config is NONE, grapped from pyfile")
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
        debug("config loaded from mapping")
    # ensure the instance folder exists
    try:
        debug("trying to make instance path directory")
        os.makedirs(app.instance_path)
        debug(f"instance path dir: `{app.instance_path}` created")
    except OSError:
        debug("os.makedirs not successful...")
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        debug("about to call 'hello world URI!")
        return 'Hello, World!'
    
    from . import db
    db.init_app(app)

    return app
