from flask import Blueprint, render_template


# Blueprint Configuration
error_bp = Blueprint(
    "error_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@error_bp.app_errorhandler(404)
def page_not_found(e):
    title = "Page not found"
    message = "The url requested was not found on the website."
    return render_template("error.html", message=message, title=title), 404


@error_bp.app_errorhandler(500)
def server_side_error(e):
    title = "Server side error"
    message = "An unexpected server side error."
    return render_template("error.html", message=message, title=title), 500