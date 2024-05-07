from db import db

class OnlineMeetingLink(db.Model):
    __tablename__ = 'online_meeting_link'

    id = db.Column(db.Integer, primary_key=True)
    meeting_link = db.Column(db.String)
    enroller_id = db.Column(db.Integer, db.ForeignKey('enroller_table.id'))

