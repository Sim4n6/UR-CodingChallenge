import bcrypt
from flask import Blueprint, flash, redirect, render_template, request, url_for

from ur_cc_app import db
from ur_cc_app.models import User

from ur_cc_app.auth.auth_forms import SignInForm, SignUpForm

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
        # get typed credentials
        name = form.name.data
        email = form.email.data
        password = form.password.data

        # generate salt and hash the password
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode("utf-8"), salt)

        #  TODO check whether it is already on the database

        # add the User to the db
        current_user = User(name=name, email=email, password=hashed,)
        db.session.add(current_user)
        db.session.commit()

        flash("Registration was successful, you can login now.", "success")
        return redirect(url_for("auth.signup"))
    return render_template("signin.html", title=title, form=form)


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    title = "Sign up"
    form = SignUpForm()
    if form.validate_on_submit():
        # get typed data
        email = form.email.data
        password = form.password.data

        # get the corresponding user based on the email
        user = User.query.filter_by(email=email).first()

        #  compare the typed password and the hashed stored password (user.password)
        if bcrypt.checkpw(password.encode("utf-8"), user.password):
            flash("Credentials are correct, you are now logged in.", "success")
            return redirect("/success")
        else:
            flash("Credentials are incorrect. Please try again.", "danger")
            return redirect(url_for("auth_bp.signup"))

    return render_template("signup.html", title=title, form=form)
