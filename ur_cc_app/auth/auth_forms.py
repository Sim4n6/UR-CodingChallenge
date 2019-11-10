from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[Length(min=2, max=100)])
    email = StringField("Email", validators=[Email()])
    password = PasswordField("Password", validators=[Length(min=6, max=120)])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[EqualTo("password", message="Passwords must match.")],
    )
    submit_button = SubmitField("Sign In")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Email()])
    password = PasswordField("Password", validators=[Length(min=6, max=120)])
    submit_button = SubmitField("Sign Up")
