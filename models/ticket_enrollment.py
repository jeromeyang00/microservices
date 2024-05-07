from db import db
from models.student import Student

class TicketEnrollment(db.Model):
    __tablename__ = 'ticket_enrollment_table'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student_table.id'))
    ticket_number = db.Column(db.String, nullable=False)
