from flask import Blueprint, render_template
from flask import current_app as app

# Blueprint Configuration
main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)


@main_bp.route("/", methods=["GET"])
@main_bp.route("/index", methods=["GET"])
def index():
    """Landing page route."""
    return render_template("index.html", title="UR-CC")


@main_bp.route("/about", methods=["GET"])
def about():
    """About page route."""
    return render_template("index.html", title="About TODO")
