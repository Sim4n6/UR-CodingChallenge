from .config import config_choices

import os

from flask import Blueprint, Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def create_app():

    app = Flask(__name__, template_folder="templates", static_folder="static")

    # load the environment configs using FLASK_CONFIG otherwise load Development.
    app.config.from_object(config_choices[os.getenv("FLASK_CONFIG") or "Development"])
    print(app.config)
    db.init_app(app)
    ma.init_app(app)
    bootstrap = Bootstrap(app)

    # register bluprints
    from ur_cc_app.main import main_routes

    app.register_blueprint(main_routes.main_bp)

    from ur_cc_app.api import api_routes

    app.register_blueprint(api_routes.api_bp)

    from ur_cc_app.errors import errors_routes

    app.register_blueprint(errors_routes.error_bp)

    return app
