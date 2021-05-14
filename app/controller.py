from flask import url_for
from app.model import users, submission, answer
from app import db
from flask_login import current_user, login_user, logout_user
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy.exc import SQLAlchemyError
import sys
from datetime import datetime


def createUser(user,password):
    if user.validate() and password!="":
        if not users.query.filter_by(username=user.username).first():
            try:
                user.set_password(password)
                db.session.add(user)
                db.session.commit()
            except SQLAlchemyError as e:
                print("user creation raised an esception:", str(e))
                return False
            return True
        else:
            print("username existed")
            return False
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
        for i in range(len(responses)):
            if not isinstance(responses[i],answer):
                raise TypeError
        try:
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
            db.session.commit()
        except SQLAlchemyError as e:
            print("submit:", str(e))
            raise TypeError
        return True
    else:
        return False

def autoMark(submission):
    intro = ["g,e","minim","b","semibreave,minim,crotchet ,quaver,semiquaver","4/4,four four"]
    intermediate = ["c#,quaver","compound,duple","six,6","gb","f#,c#,g#"]
    difficult = ["f,bb,g","f,bb,c#,d,seventh,7th,lower","no, d#","9/8,nine,eight","augmented,fourth,supertonic"]
    ans_list = getAnswerForSub(submission.id)
    for item in ans_list:
        print("item",item.submittedAnswer, item.answerSeq)
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
                print(match, i)
                orig = ans.submittedAnswer.split(" ")
                print(orig)
                for item in orig:
                    if item.lower() in match:
                        print("markReceived")
                        ans.markreceived = True
                        total += 1
                        break
        if not ans.markreceived:
            ans.markreceived = False
    submission.totalmark = total
    submission.passed = False if total < 2 else True
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        print("submit:", str(e))
        return False
    return True


def createSubmission(sid, difficulty, form):
    valid_dif = ["intro","intermediate","difficult"]
    if difficulty not in valid_dif or users.query.filter_by(id=sid).first() == None:
        raise ValueError
    sub = submission()
    sub.difficulty = difficulty
    sub.creater_id = sid
    db.session.add(sub)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        print("submit:", str(e))
        raise TypeError
    
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
        raise TypeError
    return sub





def howManySubmissions():
    sub = submission.query.all()
    return(len(sub))

def howManyUsers():
    usr = users.query.filter_by(isAdmin=False).all()
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
        return None
    else:
        return usr

def getSubmissionById(sub_id):
    this_sub = submission.query.filter_by(id=sub_id).first()
    if this_sub==None:
        print('cannot find submission with id:', sub_id)
        return None
    else:
        return this_sub

def getAnswerForSub(sub_id):
    answer_list = answer.query.filter_by(submissionId=sub_id).all()
    print(answer_list)
    if not answer_list:
        print('cannot find answer for submission:', sub_id)
        return None
    else:
        return answer_list

def getNoteRanking(userid):
    ranking = None
    adminCount = 0
    user_list = users.query.order_by(users.noteHighScore.desc()).all()
    if user_list != None:
        if user_list==None:
            print('Ranking not avaliable')
            return False
        for i in range(len(user_list)):
            if user_list[i].isAdmin:
                adminCount += 1
            if user_list[i].id == userid:
                ranking = i+1
                ranking -= adminCount
                break
        if not ranking:
            print("id not found:",userid)
            return False
        return ranking
    else:
        return False
        
def getKeyRanking(userid):
    ranking = None
    adminCount = 0
    user_list = users.query.order_by(users.KeyHighScore.desc()).all()
    if user_list != None:
        for i in range(len(user_list)):
            if user_list[i].isAdmin:
                adminCount += 1
            if user_list[i].id == userid:
                ranking = i+1
                ranking -= adminCount
                break
        if not ranking:
            print("id not found")
            return False
        return ranking
    else:
        return False


def getAdminProfile(page, userId):
    all_sub = getAllSubmissions().paginate(page, 10, False)
    ###########
    if all_sub.has_next:
        next_sub_page = url_for('index.profile', page=all_sub.next_num, userId=userId) 
    else:
        next_sub_page = None
    if all_sub.has_prev:
        prev_sub_page = url_for('index.profile', page=all_sub.prev_num, userId=userId) 
    else:
        prev_sub_page = None
    #######
    all_user = getAllUsers()
    info = {
        'subs'  : all_sub.items,
        'usrs'  : all_user,
        'subCount' : howManySubmissions(),
        'usrCount' : howManyUsers(),
        '_links': {
            'sub_prev' : prev_sub_page,
            'sub_next' : next_sub_page, 
        }
    }
    return info


def getUserProfile(page, userId):
    my_sub = submission.query.filter_by(creater_id=userId).order_by(submission.createdAt.desc()).paginate(page, 10, False)
    ###########
    if my_sub.has_next:
        next_sub_page = url_for('index.profile', page=my_sub.next_num, userId=userId) 
    else:
        next_sub_page = None
    if my_sub.has_prev:
        prev_sub_page = url_for('index.profile', page=my_sub.prev_num, userId=userId) 
    else:
        prev_sub_page = None
    info = {
        'subs'  : my_sub.items,
        'noteRank' : getNoteRanking(int(userId)),
        'notelist': getNoteList(),
        'keyRank' : getKeyRanking(int(userId)),
        'keylist':getKeyList(),
        '_links': {
            'sub_prev' : prev_sub_page,
            'sub_next' : next_sub_page, 
        }
    }
    return info


def processNoteScore(userId,score):
    this_user = getUserById(userId)
    if this_user.noteHighScore < score:
        this_user.noteHighScore = score
        db.session.commit()
        result = {
            'record': True,
            'HighScore': score,
            'ranking': getNoteRanking(userId),
            'score': score
        }
        print("result is",result)
    else:
        result = {
            'record': False,
            'HighScore': this_user.noteHighScore,
            'ranking': getNoteRanking(userId),
            'score': score
        }
        print("result is",result)
    db.session.commit()
    return result

def processKeyScore(userId,score):
    this_user = getUserById(userId)
    if this_user.KeyHighScore < score:
        this_user.KeyHighScore = score
        db.session.commit()
        result = {
            'record': True,
            'HighScore': score,
            'ranking': getKeyRanking(userId),
            'score': score
        }
        print("result is",result)
    else:
        result = {
            'record': False,
            'HighScore': this_user.KeyHighScore,
            'ranking': getKeyRanking(userId),
            'score': score
        }
        print("result is",result)
    db.session.commit()
    return result

def getNoteList():
    top_users = users.query.filter_by(isAdmin=False).order_by(users.noteHighScore.desc()).limit(7).all()
    print("users",top_users)
    return top_users

def getKeyList():
    top_users = users.query.filter_by(isAdmin=False).order_by(users.KeyHighScore.desc()).limit(7).all()
    print("users",top_users)
    return top_users