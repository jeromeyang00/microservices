from db import db

class Status(db.Model):
    __tablename__ = 'status_table'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    
