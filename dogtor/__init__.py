from flask import Flask, request
from .api import api
from .config import Config
from .db import db

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(api)

    @app.route("/init_db")
    def init_db():
        db.create_all()
        return "Database Created"

    @app.route("/home")
    @app.route("/")
    def hello():
        return "Hello Koders!"

    return app


# owners
# pets
# species
# procedures