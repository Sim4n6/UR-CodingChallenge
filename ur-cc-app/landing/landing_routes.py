from flask import Blueprint, render_template
from flask import current_app as app

# Blueprint Configuration
landing_bp = Blueprint(
    "landing_bp", __name__, template_folder="templates", static_folder="static"
)


@landing_bp.route("/", methods=["GET"])
@landing_bp.route("/index", methods=["GET"])
def home():
    """Landing page route."""
    return render_template("index.html", title="UR-CC")


@landing_bp.route("/about", methods=["GET"])
def about():
    """About page route."""
    return render_template("index.html", title="About TODO")
