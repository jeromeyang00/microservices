from db import db


class Student(db.Model):
    __tablename__ = 'student_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    student_number = db.Column(db.String)
    mode_id = db.Column(db.Integer, db.ForeignKey('modes_table.id'))
    department_id = db.Column(db.Integer, db.ForeignKey('department_table.id'))
    enrollments = db.relationship('EnrollAssignment', backref='student', lazy=True)

class Status(db.Model):
    __tablename__ = 'status_table'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)

class Mode(db.Model):
    __tablename__ = 'modes_table'
    id = db.Column(db.Integer, primary_key=True)
    mode = db.Column(db.String, nullable=False)
    enrollers = db.relationship('Enroller', backref='mode', lazy=True)
    students = db.relationship('Student', backref='mode', lazy=True)


class OnlineMeetingLink(db.Model):
    __tablename__ = 'online_meeting_link'
    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department_table.id'))

class Department(db.Model):
    __tablename__ = 'department_table'
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String)
    students = db.relationship('Student', backref='department', lazy=True)
    enrollers = db.relationship('Enroller', backref='department', lazy=True)
    online_meeting_link = db.relationship('OnlineMeetingLink', backref='department', lazy=True)

class TicketEnrollment(db.Model):
    __tablename__ = 'ticket_enrollment_table'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student_table.id'))
    ticket_number = db.Column(db.Integer)

class Sem(db.Model):
    __tablename__ = 'sem_table'
    id = db.Column(db.Integer, primary_key=True)
    sem = db.Column(db.Integer)

class EnrollAssignment(db.Model):
    __tablename__ = 'enrollment_assignment_table'
    id = db.Column(db.Integer, primary_key=True)
    enroller_name_id = db.Column(db.Integer, db.ForeignKey('enroller_table.id'))
    student_name_id = db.Column(db.Integer, db.ForeignKey('student_table.id'))
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket_enrollment_table.id'))
    status_id = db.Column(db.String, db.ForeignKey('status_table.status.id'))

