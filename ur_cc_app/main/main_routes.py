from flask import Blueprint
from flask import current_app as app
from flask import render_template

import requests

# Blueprint Configuration
main_bp = Blueprint(
    "main_bp",
    __name__,
    url_prefix="/main",
    template_folder="templates",
    static_folder="static",
)


@main_bp.route("/nearby", methods=["GET"])
def nearby():
    """Nearby shops page."""

    r = requests.get("http://localhost:5000/api/shops") # FIXME prepare an url independant from localhost
    all_shops = r.json()

    return render_template("nearby.html", title="Nearby shops", all_shops=all_shops)


@main_bp.route("/preferred", methods=["GET"])
def preferred():
    """Preferred shops page."""
    return render_template("preferred.html", title="Preferred shops")
