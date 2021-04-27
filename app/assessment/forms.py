from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class submissionForm(FlaskForm):
    Q1 = RadioField(
        'Question1',
        validators=[DataRequired()],
        choices=[
            ('1', 'C'),
            ('2', 'D'),
            ('3', 'E'),
            ('4', 'F'),
        ]
    )
    Q1ans = StringField("Question1Ans")
    submit = SubmitField('submit')

    