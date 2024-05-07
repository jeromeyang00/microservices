from marshmallow import Schema, fields

class EnrollerSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    assigned_mode_id = fields.Integer(required=True)
    enroller_number = fields.String(required=True)
    department_id = fields.Integer(required=True)

class ModeSchema(Schema):
    id = fields.Integer()
    mode = fields.String(required=True)
    enrollers = fields.Nested('EnrollerSchema', many=True)
    students = fields.Nested('StudentSchema', many=True)

class StudentSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    student_number = fields.String(required=True)
    department_id = fields.Integer()
    mode_id = fields.Integer()
    enrollments = fields.Nested('EnrollAssignmentSchema', many=True)

class StudentModesSchema(Schema):
    student_number = fields.String(required=True)
    modes = fields.String(required=True)

class SemSchema(Schema):
    id = fields.Integer(required=True)
    sem = fields.Integer(required=True)

class StatusSchema(Schema):
    id = fields.Integer(required=True)
    status = fields.String(required=True)

class DepartmentSchema(Schema):
    id = fields.Integer()
    department = fields.String()
    students = fields.Nested('StudentSchema', many=True)
    online_meeting_links = fields.Nested('OnlineMeetingLinkSchema', many=True)

class OnlineMeetingLinkSchema(Schema):
    id = fields.Integer()
    meeting_link = fields.String()
    enroller = fields.String()

class TicketGenerateSchema(Schema):
    student_number = fields.String(required=True)

class TicketEnrollmentSchema(Schema):
    id = fields.Integer()
    student_id = fields.Integer(required=True)
    ticket_number = fields.String()

class EnrollAssignmentSchema(Schema):
    id = fields.Integer(required=True)
    enroller_name_id = fields.Integer()
    student_name_id = fields.Integer()
    ticket_id = fields.Integer()
    status_id = fields.String()
    department_id = fields.Integer()
