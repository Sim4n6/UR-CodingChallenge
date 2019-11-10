from flask import Blueprint, render_template, redirect, request

from .auth_forms import SignInForm, SignUpForm

# Blueprint Configuration
auth_bp = Blueprint(
    "auth_bp",
    __name__,
    url_prefix="/auth",
    template_folder="templates",
    static_folder="static",
)


@auth_bp.route("/signin", methods=["GET", "POST"])
def signin():
    title = "Sign in"
    form = SignInForm()
    if form.validate_on_submit():
        return redirect("/success")
    return render_template("signin.html", title=title, form=form)


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    title = "Sign up"
    form = SignUpForm()
    if form.validate_on_submit():
        return redirect("/success")
    return render_template("signup.html", title=title, form=form)
