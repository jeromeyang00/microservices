from db import db
from models.department import Department

class Sem(db.Model):
    __tablename__ = 'sem_table'
    id = db.Column(db.Integer, primary_key=True)
    sem = db.Column(db.Integer, nullable=False)