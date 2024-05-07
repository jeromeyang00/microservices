from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import jsonify
from models import Student, Department, Enroller, Mode
from schema import EnrollerSchema
from db import db

from sqlalchemy.exc import IntegrityError, SQLAlchemyError


enroller_blp = Blueprint('enroller', __name__, description='Enroller operations')

@enroller_blp.route('/enrollers')
class EnrollerListView(MethodView):
        
        @enroller_blp.response(200, EnrollerSchema)
        def get(self):
            # Fetch all students from the database
            enrollers = Enroller.query.all()
            
            # Convert each student to a dictionary representation

            enrollers_data = []

            
            for enroller in enrollers:
                
                print(enroller.assigned_mode_id)
                print(enroller.department_id)
                print(enroller.enroller_number)
                print(enroller.name)
                print(enroller.id)
                enroller_mode = Mode.query.filter_by(id=enroller.assigned_mode_id).first(); #student_num is string
                department = Department.query.filter_by(id=enroller.department_id).first()

                enroller_data = {
                    "id": enroller.id,
                    "name": enroller.name,
                    "assigned_mode": enroller_mode.mode,
                    "department_id": department.department,
                    "enroller_number": enroller.enroller_number
                }
                enrollers_data.append(enroller_data)
    
            # Return the list of student dictionaries as JSON
            return jsonify(enrollers=enrollers_data)

@enroller_blp.route('/enroller_create')
class CreateEnroller(MethodView):
    @enroller_blp.arguments(EnrollerSchema)
    @enroller_blp.response(201, EnrollerSchema)
    def post(self, data):
        data = Enroller(**data)
        try:
            db.session.add(data)
            db.session.commit()
        except IntegrityError:
            abort(409, message="Enroller already exists")
        except SQLAlchemyError as e:
            abort(500, message=f"Internal server error: {e}")

        return {"message": "Enroller created successfully"}, 201
    

@enroller_blp.route('/enroller/<string:enroller_num>')
class FindEnroller(MethodView):
    @enroller_blp.response(200, EnrollerSchema)
    def get(self, enroller_num):
        enroller = Enroller.query.filter_by(enroller_number=enroller_num).first()
        if enroller is None:
            abort(404, message="Enroller not found")

        enroller_mode = Mode.query.filter_by(id=enroller.assigned_mode_id).first(); #student_num is string
        department = Department.query.filter_by(id=enroller.department_id).first()

        enroller_data = {
                    "id": enroller.id,
                    "name": enroller.name,
                    "assigned_mode": enroller_mode.mode,
                    "department_id": department.department,
                    "enroller_number": enroller.enroller_number
                }        
        
        return jsonify(enroller=enroller_data)
