from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={
                           "placeholder": "Username"})
    password = PasswordField('Password', validators=[DataRequired(), length(min=6, max=80)], render_kw={
        "placeholder": "Username"})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
