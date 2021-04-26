from app import db, login
from flask_login import UserMixin

class users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(96), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    firstname = db.Column(db.String(130), nullable=False)
    lastname = db.Column(db.String(130), nullable=False)

    isActive = db.Column(db.Boolean)
    def __init__(self):
        self.isActive = True
    def __repr__(self):
        return '<User %r>' % self.username



@login.user_loader
def load_user(usr_id):
    return users.query.get(int(usr_id))