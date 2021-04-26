from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, length

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),length(min=6, max=80)])
    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(),length(min=6, max=80)])
    email = StringField("email", validators=[DataRequired(),Email()])
    submit = SubmitField('Sign up')