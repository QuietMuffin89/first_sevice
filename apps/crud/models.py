from apps.app import db

class User(db.Model):
    __tablename__ = "webtoons"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, index=True)
    author = db.Column(db.String, index=True)
    genre = db.Column(db.String, index=True)
    link = db.Column(db.String, index=True)