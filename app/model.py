from app import db, login
from flask_login import UserMixin
from datetime import datetime
from flask import url_for, redirect

class users(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(96), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    firstname = db.Column(db.String(130), nullable=False)
    lastname = db.Column(db.String(130), nullable=False)
    lastLogin = db.Column(db.DateTime)
    isActive = db.Column(db.Boolean)
    isAdmin = db.Column(db.Boolean)
    noteHighScore = db.Column(db.Integer)
    KeyHighScore = db.Column(db.Integer)
    submit = db.relationship("submission", backref="submitter")

    ###################################################
    
    def __init__(self):
        self.isActive = True
        self.isAdmin = False
        self.noteHighScore = 0
        self.lastLogin = None
        self.KeyHighScore = 0
    
    def is_active(self):
        return self.isActive

    def validate(self):
        if self.username and self.email and self.firstname and self.lastname:
            return True

    #@staticmethod
    def getSubmissions(self):
        res = submission.query.filter_by(creater_id=self.id).all()
        return res

    def __repr__(self):
        return '<user %r>' % self.username

class submission(db.Model):
    
    __tablename__ = 'submission'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    createdAt = db.Column(db.DateTime)
    markedAt = db.Column(db.DateTime)
    feedback = db.Column(db.Boolean)
    totalmark = db.Column(db.Integer)
    difficulty = db.Column(db.String(30))
    passed = db.Column(db.Boolean)
    creater_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    answers = db.relationship("answer", backref="submission")

    def __init__(self):
        self.createdAt = datetime.utcnow()
        self.markedAt = None
        self.totalmark = None
        self.marked = False
        self.passed = False
        print("submission init")
    
    def validate(self):
        if self.difficulty and self.creater_id and self.createdAt:
            return True

    def __repr__(self):
        return '<submission %r>' % self.id
    
        
class answer(db.Model):
    __tablename__ = 'answer'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    answerSeq = db.Column(db.Integer)
    submittedAnswer = db.Column(db.String(400))
    feedback = db.Column(db.String(400))
    markreceived = db.Column(db.Boolean)
    submissionId = db.Column(db.Integer, db.ForeignKey("submission.id"))

    def __init__(self):
        feedback = None
        markreceived = 1

    def validate(self):
        if self.answerSeq and self.submittedAnswer and submissionId:
            return True
        else:
            print("missingfield")
            return False
    def __repr__(self):
        return '<ans>'


@login.user_loader
def load_user(usr_id):
    return users.query.get(int(usr_id))


@login.unauthorized_handler
def unauthorized():
    return redirect(url_for("index.index"))

#.headers on
#.open app.db
#.mode column
#select * from submission;