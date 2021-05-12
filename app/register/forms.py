from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),length(min=6, max=80)])
    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(),length(min=6, max=80), EqualTo('password')])
    email = StringField("email", validators=[DataRequired(),Email()])
    submit = SubmitField('Sign up')
    
    def username_validate(self, username):
        usr = users.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please enter a different username.')

    def email_validate(self, email):
        usr = users.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please enter a different email address.')
    
    def password_validate(self, password):
        if len(password) < 6:
            raise ValidationError("Password has to be atleast 6 characters long")