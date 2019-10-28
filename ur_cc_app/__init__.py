import os

from flask import Blueprint, Flask, jsonify, make_response, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():

    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    Bootstrap(app)

    # register bluprints
    from ur_cc_app.main import main_routes

    app.register_blueprint(main_routes.main_bp)

    from ur_cc_app.api import api_routes

    app.register_blueprint(api_routes.api_bp)

    return app
