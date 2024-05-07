
from db import db
from models.department import Department

class Student(db.Model):
    __tablename__ = 'student_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    student_number = db.Column(db.String)
    mode_id = db.Column(db.Integer, db.ForeignKey('modes_table.id'))
    department_id = db.Column(db.Integer, db.ForeignKey('department_table.id'), nullable=False)

    

