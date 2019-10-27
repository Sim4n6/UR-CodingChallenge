from flask import Blueprint, render_template
from flask import current_app as app

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
    return render_template("nearby.html", title="Nearby shops")


@main_bp.route("/preferred", methods=["GET"])
def preferred():
    """Preferred shops page."""
    return render_template("preferred.html", title="Preferred shops")
