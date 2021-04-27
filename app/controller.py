from app.model import users, submission, answer
from app import db
from flask_login import current_user, login_user, logout_user
from sqlalchemy.orm.attributes import flag_modified
from datetime import datetime

def getAllans():
    answers = answer.query.all()
    lis = []
    for item in answers:
        lis.append(item.sumbittedAnswer)
    return lis
    #anse = sub1.answers[0].sumbittedAnswer
    #ans = int(form.Q1ans.data)