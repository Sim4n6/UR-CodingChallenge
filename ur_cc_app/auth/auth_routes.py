from flask import Blueprint, render_template


# Blueprint Configuration
auth_bp = Blueprint(
    "auth_bp",
    __name__,
    url_prefix="/auth",
    template_folder="templates",
    static_folder="static",
)


@auth_bp.route("/signup")
def signup():
    title = "Sign up"
    return render_template("signin.html", title=title)


@auth_bp.route("/signin")
def signin():
    title = "Sign in"
    return render_template("signin.html", title=title)
