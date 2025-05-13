from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=None)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE
    )