from app.model import users, submission
from app import db
from flask_login import current_user, login_user, logout_user
from sqlalchemy.orm.attributes import flag_modified
from datetime import datetime

def getAllans():
    submissions = submission.query.all()
    lis = []
    for item in submissions:
        a = item.answers[0].sumbittedAnswer
        lis.append(a)
    return lis
    #anse = sub1.answers[0].sumbittedAnswer
    #ans = int(form.Q1ans.data)