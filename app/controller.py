from app.model import users, submission, answer
from app import db
from flask_login import current_user, login_user, logout_user
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash
import sys
from datetime import datetime


def createUser(user,password):
    if user.validate():
        hash_pwd = generate_password_hash(password, method="sha384")
        user.password = hash_pwd
        db.session.add(user)
        db.session.commit()
        return True
    else:
        print("Missing data")
        return False

# removes user and corrospoding 
def removeUser(userId):
    if not userId:
        print("Unknown id provided")
        return False
    else:
        this_user = getUserById(userId)
        sub_of_user =  this_user.getSubmissions()
        ans_of_user = []
        for sub in sub_of_user:
            ans_list = getAnswerForSub(sub.id)
            for ans in ans_list:
                ans_of_user.append(ans)
    
        try:
            for sub in sub_of_user:
                db.session.delete(sub)
            for ans in ans_of_user:
                db.session.delete(ans)
            db.session.delete(this_user)
            db.session.commit()
        except SQLAlchemyError as e:
            print("update login time raised exception:", str(e))
            return False
        return True

def updateLoginTime(user):
    if user:
        user.lastLogin = datetime.utcnow()
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError as e:
            print("update login time raised exception:", str(e))
            return False
        return True
    else:
        print("invalid user Object")
        return False

def feedbackAssessment(sub,form,responses):
    if sub and form and responses:
        for item in responses:
            if item.answerSeq == 1:
                item.feedback = form.F1.data
            elif item.answerSeq == 2:
                item.feedback = form.F2.data
            elif item.answerSeq == 3:
                item.feedback = form.F3.data
            elif item.answerSeq == 4:
                item.feedback = form.F4.data
            elif item.answerSeq == 5:
                item.feedback = form.F5.data
            db.session.add(item)
        sub.markedAt = datetime.utcnow()
        sub.feedback = True
        db.session.add(sub)
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            print("submit:", str(e))
            return False
        return True
    else:
        print("missing object")
        return False

def autoMark(submission):
    intro = ["g,e","minim","b","semibreave,minim,crotchet ,quaver,semiquaver","4/4,four four"]
    intermediate = ["c#,quaver","compound,duple","six,6","gb","f#,c#,g#"]
    difficult = ["f,bb,g","f,bb,c#,d,seventh,7th,lower","no, d#","9/8,nine,eight","augmented,fourth,supertonic"]
    ans_list = getAnswerForSub(submission.id)
    if submission.difficulty == "intro":
        index = intro
    elif submission.difficulty == "intermediate":
        index = intermediate
    elif submission.difficulty == "difficult":
        index = difficult
    else:
        print("unknown difficulty")
        return False
    total = 0
    for ans in ans_list:
        for i in range(len(index)):
            if i == ans.answerSeq-1:
                match = index[i].split(",")
                print(match)
                orig = ans.submittedAnswer.split(" ")
                print(orig)
                for item in orig:
                    if item.lower() in match:
                        ans.markreceived = True
                        total += 1
                        break
    submission.totalmark = total
    print(total)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        print("submit:", str(e))
        return False
    return True


def createSubmission(sid, difficulty, form):
    sub = submission()
    sub.difficulty = difficulty
    sub.creater_id = sid
    db.session.add(sub)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        print("submit:", str(e))
        return None
    
    ans1 = answer()
    ans1.answerSeq=1
    ans1.submittedAnswer = form.Q1.data
    ans1.submissionId = sub.id

    ans2 = answer()
    ans2.answerSeq=2
    ans2.submittedAnswer = form.Q2.data
    ans2.submissionId = sub.id
    
    ans3 = answer()
    ans3.answerSeq=3
    ans3.submittedAnswer = form.Q3.data
    ans3.submissionId = sub.id

    ans4 = answer()
    ans4.answerSeq=4
    ans4.submittedAnswer = form.Q4.data
    ans4.submissionId = sub.id

    ans5 = answer()
    ans5.answerSeq=5
    ans5.submittedAnswer = form.Q5.data
    ans5.submissionId = sub.id



    db.session.add(ans1)
    db.session.add(ans2)
    db.session.add(ans3)
    db.session.add(ans4)
    db.session.add(ans5)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        print("submit:", str(e))
        return None
    return sub





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
    alluser = users.query.order_by(users.lastLogin.desc()).all()
    return alluser

def getUserById(userId):
    usr = users.query.filter_by(id=userId).first()
    if usr==None:
        print('cannot find user with id:', userId)
        return False
    else:
        return usr

def getSubmissionById(sub_id):
    this_sub = submission.query.filter_by(id=sub_id).first()
    if this_sub==None:
        print('cannot find submission with id:', sub_id)
        return False
    else:
        return this_sub

def getAnswerForSub(sub_id):
    answer_list = answer.query.filter_by(submissionId=sub_id).all()
    print(answer_list)
    if not answer_list:
        print('cannot find answer for submission:', sub_id)
        return False
    else:
        return answer_list

def getNoteRanking(userid):
    ranking = None
    user_list = users.query.order_by(users.noteHighScore.desc()).all()
    if user_list==None:
        print('Ranking not avaliable')
        return False
    for i in range(len(user_list)):
        if user_list[i].id == userid:
            ranking = i+1
            break
    if not ranking:
        print("id not found:",userid)
        return False
    return ranking

def getKeyRanking(userid):
    ranking = None
    user_list = users.query.order_by(users.KeyHighScore.desc()).all()
    print(user_list)
    for i in range(len(user_list)):
        print("list",type(user_list[i].id))
        print("user",type(userid))
        if user_list[i].id == userid:
            ranking = i+1
            break
    if not ranking:
        print("id not found")
        return False
        print(ranking)
    return ranking