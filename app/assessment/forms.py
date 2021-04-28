from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class submissionForm(FlaskForm):
    Q1 = TextAreaField("Question1")
    Q2 = TextAreaField("Question2")
    submit = SubmitField("submit")



class markingForm(FlaskForm):
    F1 = TextAreaField("Feedback1")
    F2 = TextAreaField("Feedback2")
    submit = SubmitField("submit")

