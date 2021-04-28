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

    print(type(sub_id), sub_id)
    this_sub = submission.query.filter_by(id=sub_id).first()
    print("this sub is",this_sub)
    return this_sub


def getAnswerForSub(sub_id):
    answer_list = answer.query.filter_by(submissionId=sub_id).all()
    return answer_list


def getAllUserResponse(userId):
    if userId != None:
        try:
            res = submission.query.filter_by(creater_id=userId).all()
        except:
            print("no answer exist")
            return False
        return res
    
