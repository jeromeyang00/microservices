from db import db

class Department(db.Model):
    __tablename__ = 'department_table'
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String)
    students = db.relationship('Student', backref='department', lazy=True)
    enrollers = db.relationship('Enroller', backref='department', lazy=True)
