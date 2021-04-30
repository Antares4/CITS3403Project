from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, length

class submissionForm(FlaskForm):
    Q1 = TextAreaField("Question1", validators=[DataRequired()])
    Q2 = TextAreaField("Question2", validators=[DataRequired()])
    Q3 = TextAreaField("Question3", validators=[DataRequired()])
    Q4 = TextAreaField("Question4", validators=[DataRequired()])
    Q5 = TextAreaField("Question5", validators=[DataRequired()])
    submit = SubmitField("submit")

class markingForm(FlaskForm):
    F1 = TextAreaField("Feedback1")
    F2 = TextAreaField("Feedback2")
    F3 = TextAreaField("Feedback3")
    F4 = TextAreaField("Feedback4")
    F5 = TextAreaField("Feedback5")
    submit = SubmitField("submit")

