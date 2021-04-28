from app.model import users, submission, answer
from app import db
from flask_login import current_user, login_user, logout_user
from sqlalchemy.orm.attributes import flag_modified
from datetime import datetime




def getAllSubmissions():
    try:
        all_sub = submission.query.all()
    except:
        print("submission does not exist")
        return False
    return all_sub

def getSubmissionById(sub_id):
    try:
        this_sub = submission.query.filter_by(id=sub_id).first()
    except:
        print("submission does not exist")
        return False
    return this_sub

def adminAuthen():
    #static 
    pass

def getAllUserResponse(sub):
    if sub != None:
        try:
            res = answer.query.filter_by(id=sub.get_id()).all()
        except:
            print("no answer exist")
            return False
        return res
    


