from app import db

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(100))

    def __init__(self):
        self.name=None
        self.password=None
    def __repr__(self):
        return '<User %r>' % self.username