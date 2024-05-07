from db import db

class Mode(db.Model):
    __tablename__ = 'modes_table'
    id = db.Column(db.Integer, primary_key=True)
    mode = db.Column(db.String, nullable=False)
    enrollers = db.relationship('Enroller', backref='mode', lazy=True)