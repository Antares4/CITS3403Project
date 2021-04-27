from app import db, login
from flask_login import UserMixin
from datetime import datetime

class users(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(96), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    firstname = db.Column(db.String(130), nullable=False)
    lastname = db.Column(db.String(130), nullable=False)
    isActive = db.Column(db.Boolean)
    submit = db.relationship("submission", backref="submitter")
    
    ###################################################
    
    def __init__(self):
        self.isActive = True
    
    def is_active(self):
        return True

    def get_id(self):
        return self.id
    
    def __repr__(self):
        return '<user %r>' % self.username

class submission(db.Model):
    
    __tablename__ = 'submission'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.String)
    # createdAt = db.Column(db.DateTime)
    # lastModifiedAt = db.Column(db.DateTime)
    # completedAt = db.Column(db.DateTime)
    creater_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    answers = db.relationship("answer", backref="submission")
    def __init__(self):
        print("submission init")
    
    # def addAnswers(self, userAnswer):
    #     if userAnswer == None:
    #         print('useranswer needed!')
    #         return False
    #     else:
    #         this_answer = submission.answer()
    #         this_answer.sumbittedAnswer = userAnswer
    #         print("useranswer is",userAnswer)
    #         this_answer.correctAnswer = 1
    #         self.answers.append(this_answer)

class answer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    answerSeq = db.Column(db.Integer)
    sumbittedAnswer = db.Column(db.Integer)
    correctAnswer = db.Column(db.Integer)
    submissionId = db.Column(db.Integer, db.ForeignKey("submission.id"))
    
    def __init__(self):
        print("init answers")
    def __repr__(self):
        return '<ans>'

@login.user_loader
def load_user(usr_id):
    return users.query.get(int(usr_id))



#.headers on
#.open app.db
#.mode column
#select * from submission;