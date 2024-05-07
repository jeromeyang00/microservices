from models.department import Department
from models.modes import Mode

from db import db

class Enroller(db.Model):
    __tablename__ = 'enroller_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    assigned_mode_id = db.Column(db.Integer, db.ForeignKey('modes_table.id'), nullable=False)
    enroller_number = db.Column(db.String, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department_table.id'), nullable=False)
    meeting_link=db.relationship('OnlineMeetingLink', backref='enroller', lazy=True)

    # Access an Enroller record based on assigned_mode_id and department_id
    # @classmethod
    # def find_by_mode_and_department(cls, mode_id, department_id):
    #     return cls.query.filter_by(assigned_mode_id=mode_id, department_id=department_id).first()