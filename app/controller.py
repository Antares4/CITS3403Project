from app.model import users, submission, answer
from app import db
from flask_login import current_user, login_user, logout_user
from sqlalchemy.orm.attributes import flag_modified
from datetime import datetime


def howManySubmissions():
    sub = submission.query.all()
    return(len(sub))

def howManyUsers():
    usr = users.query.all()
    return(len(usr))

def getAllSubmissions():
    all_sub = submission.query.order_by(submission.createdAt.desc())
    return all_sub

def getAllUsers():
    alluser = users.query.order_by(users.joinedAt.asc()).all()
    return alluser

def getUserById(userId):
    usr = users.query.filter_by(id=userId).first()
    if usr==None:
        print('cannot find the user with id:', userId)
        return False
    else:
        return usr

def getSubmissionById(sub_id):
    this_sub = submission.query.filter_by(id=sub_id).first()
    return this_sub

def getAnswerForSub(sub_id):
    answer_list = answer.query.filter_by(submissionId=sub_id).all()
    return answer_list

def getNoteRanking(userid):
    user_list = users.query.order_by(users.noteHighScore.desc()).all()
    print(user_list)
    for i in range(len(user_list)):
        if user_list[i].id == userid:
            ranking = i+1
            break
    if not ranking:
        print("id not found")
        return False
        print(ranking)
    return ranking

def getKeyRanking(userid):
    user_list = users.query.order_by(users.KeyHighScore.desc()).all()
    print(user_list)
    for i in range(len(user_list)):
        if user_list[i].id == userid:
            ranking = i+1
            break
    if not ranking:
        print("id not found")
        return False
        print(ranking)
    return ranking