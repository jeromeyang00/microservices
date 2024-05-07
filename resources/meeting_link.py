from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import jsonify
from models import Student, Department, Enroller, Mode, OnlineMeetingLink
from schema import OnlineMeetingLinkSchema, EnrollerSchema
from db import db

from sqlalchemy.exc import IntegrityError, SQLAlchemyError

meeting_link_blp = Blueprint("online_meeting_link", __name__, description="Meeting Link Operation")

@meeting_link_blp.route('/get_link/<string:Enroller_name>')
class EnrollerLink(MethodView):
    def get(self, Enroller_name):
        enroller = Enroller.query.filter_by(name=Enroller_name).first()
        id = enroller.id
        data = OnlineMeetingLink.query.filter_by(enroller_id=id).first()
        meeting_link = data.meeting_link

        if data is None:
            abort(404, message="Enroller Meeting Link not found")

        # if enroller is None:
        #     abort(404, message="Enroller not found")

        # enroller = Enroller.query.filter_by(id=enroller_id).first()
        
        # return {"Enroller.id": enroller.name, "Meeting Link": data.zoom_link}

        return {"meeting_link": meeting_link, "enroller": Enroller_name}

    def delete(self,Enroller_name):
        try:
            enroller = Enroller.query.filter_by(id=Enroller_name).delete()
        except IntegrityError:
            abort(404, message="Enroller not found")

        return{"message": "Meeting Link deleted successfully"}, 201

@meeting_link_blp.route('/meeting_link')
class CreateLink(MethodView):
    def get(self):
        # Fetch all students from the database
        meeting_links = OnlineMeetingLink.query.all()
        
        # Convert each student to a dictionary representation
        meeting_links_data = []
        for meeting_link in meeting_links:
            meeting_link_data = {
                "id": meeting_link.id,
                "meeting_link": meeting_link.meeting_link,
                "enroller_id": meeting_link.enroller_id
            }
            meeting_links_data.append(meeting_link_data)

        # Return the list of student dictionaries as JSON
        return jsonify(meeting_links=meeting_links_data)

    @meeting_link_blp.arguments(OnlineMeetingLinkSchema)
    @meeting_link_blp.response(201, OnlineMeetingLinkSchema)
    def post(self, data):
        #   data = OnlineMeetingLink(**data)
        print(data)
        try:
            enroller = Enroller.query.filter_by(name=data['enroller']).first()
        except IntegrityError:
            abort(404, message="Enroller not found")
        
        name = OnlineMeetingLink.query.filter_by(name=data['enroller']).first()

        if name is not None:
            abort(409, message="Enroller already has a meeting link")

        try:
            meeting_link = OnlineMeetingLink(meeting_link=data['meeting_link'], enroller_id=enroller.id)
            db.session.add(meeting_link)
            db.session.commit()
        except IntegrityError:
            abort(409, message="Meeting Link already exists")

        return {"message": "Meeting Link created successfully"}, 201


    @meeting_link_blp.arguments(OnlineMeetingLinkSchema)
    @meeting_link_blp.response(201, OnlineMeetingLinkSchema)
    def put(self, data):
        print(data)
        try:
            enroller = Enroller.query.filter_by(name=data['enroller'])
        except IntegrityError:
            abort(404, message="Enroller not found")
        
        #updates the meeting link
        try:
            meeting_link = OnlineMeetingLink.query.filter_by(enroller_id=enroller.id).first()
            meeting_link.meeting_link = data['meeting_link']
            db.session.commit()
        except IntegrityError:
            abort(409, message="Meeting Link already exists")

        return{"message": "Meeting Link updated successfully"}, 201
    


