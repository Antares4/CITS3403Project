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
    isAdmin = db.Column(db.Boolean)
    submit = db.relationship("submission", backref="submitter")

    ###################################################
    
    def __init__(self):
        self.isActive = True
        self.isAdmin = False
    
    def is_active(self):
        return True

    def allSubmissions():
        subs = submission().query.filter_by(creater_id=self.id).all()
        return (sub)
        
    def get_id(self):
        return self.id
    
    def __repr__(self):
        return '<user %r>' % self.username

class submission(db.Model):
    
    __tablename__ = 'submission'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    createdAt = db.Column(db.DateTime)
    markedAt = db.Column(db.DateTime)
    creater_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    marked = db.Column(db.Boolean)
    difficulty = db.Column(db.String(30))
    answers = db.relationship("answer", backref="submission")

    def __init__(self):
        self.createdAt = datetime.utcnow()
        self.markedAt = None
        self.marked = False
        print("submission init")
    
    def get_id(self):
        return self.id
        
class answer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    answerSeq = db.Column(db.Integer)
    sumbittedAnswer = db.Column(db.String(400))
    feedback = db.Column(db.String(400))
    submissionId = db.Column(db.Integer, db.ForeignKey("submission.id"))
    
    def __init__(self):
        feedback = None
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