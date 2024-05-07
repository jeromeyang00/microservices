from db import db
from models.enroller import Enroller
from models.student import Student
from models.ticket_enrollment import TicketEnrollment
from models.status import Status
from models.department import Department

class EnrollAssignment(db.Model):
    __tablename__ = 'enrollment_assignment_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    enroller_name_id = db.Column(db.Integer, db.ForeignKey('enroller_table.id'))
    student_name_id = db.Column(db.Integer, db.ForeignKey('student_table.id'))
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket_enrollment_table.id'))
    status_id = db.Column(db.String, db.ForeignKey('status_table.id'))
    department_id = db.Column(db.Integer, db.ForeignKey('department_table.id'))

    
    #    meeting_link=db.relationship('OnlineMeetingLink', backref='enroller', lazy=True)


# C:\Users\Jerome Yang\OneDrive - Mapúa University\Documents\GitHub\CPE177P_C1_3Q2324_Group01_Project\models\enrollment,py