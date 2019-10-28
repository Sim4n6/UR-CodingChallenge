from flask import Blueprint, render_template, jsonify


# Blueprint Configuration
error_bp = Blueprint(
    "error_bp", __name__, template_folder="templates", static_folder="static"
)


# 4xx Clients errors
@error_bp.app_errorhandler(400)
def page_not_found(e):
    title = f"Bad request - {e.code}"
    message = str(e.description)
    return render_template("error.html", message=message, title=title), 404


@error_bp.app_errorhandler(404)
def page_not_found(e):
    title = f"Requested URL not found - {e.code}"
    message = str(e.description)
    return render_template("error.html", message=message, title=title), 404


@error_bp.app_errorhandler(403)
def page_not_found(e):
    title = f"Access forbidden - {e.code}"
    message = str(e.description)
    return render_template("error.html", message=message, title=title), 403


# 5xx Server errors
@error_bp.app_errorhandler(500)
def server_side_error(e):
    title = f"Server side error - {e.code}"
    message = str(e.description)
    return render_template("error.html", message=message, title=title), 500
