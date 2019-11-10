import bcrypt
from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    session,
    g,
)

from ur_cc_app import db
from ur_cc_app.auth.auth_forms import LoginForm, RegistrationForm
from ur_cc_app.models import User

# Blueprint Configuration
auth_bp = Blueprint(
    "auth_bp",
    __name__,
    url_prefix="/auth",
    template_folder="templates",
    static_folder="static",
)


@auth_bp.route("/registration", methods=["GET", "POST"])
def registration():
    title = "Registration"
    form = RegistrationForm()
    if form.validate_on_submit():
        # get typed credentials
        name = form.name.data
        email = form.email.data
        password = form.password.data

        # generate salt and hash the password
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode("utf-8"), salt)

        # check whether the user is already on the database
        result = User.query.filter_by(email=email).one_or_none()
        if result is None:
            # add the User to the db
            current_user = User(name=name, email=email, password=hashed)
            db.session.add(current_user)
            db.session.commit()

            flash("Registration was successful, you can login now.", "success")
            return redirect(url_for("auth_bp.login"))
        else:
            flash(
                f"User with the same email as {email} already exists. You can login if it's you.",
                "warning",
            )
            return redirect(url_for("auth_bp.login"))

    return render_template("registration.html", title=title, form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    title = "Log in"
    form = LoginForm(request.form)
    if form.validate_on_submit():
        # get typed data
        email = form.email.data
        password = form.password.data

        # get the corresponding user based on the email
        user = User.query.filter_by(email=email).one_or_none()
        # if email not in the db
        if user is None:
            flash("User not registred yet. Please register.", "warning")
            redirect(url_for("auth_bp.registration"))
        else:
            #  compare the typed password and the hashed stored password (user.password)
            if bcrypt.checkpw(password.encode("utf-8"), user.password):
                flash("Credentials are correct, you are now logged in.", "success")
                session["username"] = {
                    "name": user.name,
                    "email": email,
                }  # FIXME be careful about this pitfull.
                return redirect(url_for("landing"))
            else:
                flash("Credentials are incorrect. Please try again.", "danger")
                return redirect(url_for("auth_bp.login"))

    return render_template("login.html", title=title, form=form)


@auth_bp.route("/logout", methods=["GET"])
def logout():
    flash("You have been logged out.", "warning")
    session.pop("username", None)
    return redirect(url_for("auth_bp.login"))


@auth_bp.before_app_request
def before_request():
    g.user = None
    if "username" in session:
        g.user = session["username"]
