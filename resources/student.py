from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import jsonify
from models import Student, Department, Mode, TicketEnrollment, Sem, EnrollAssignment, Enroller
from schema import StudentSchema, StudentModesSchema, TicketGenerateSchema
from db import db

from sqlalchemy.exc import IntegrityError, SQLAlchemyError


student_blp = Blueprint('EECE Students', __name__, description='Student operations')

@student_blp.route('/students')
class StudentListView(MethodView):
    
    @student_blp.response(200, StudentSchema)
    def get(self):
        # Fetch all students from the database
        students = Student.query.all()
        
        # Convert each student to a dictionary representation
        students_data = []
        for student in students:
            #try except without abort
            try:
                print("NAME:",student.name)

                mode = Mode.query.filter_by(id=student.mode_id).first()
                if mode is None:
                    mode = None
                print("MODE:", mode.mode)
                department = Department.query.filter_by(id=student.department_id).first()
                if department is None:
                    department = None
                print("DEPARTMENT:", department.department)
            except Exception as e:
                print(e)
                print("Error in fetching mode and department")
            # department = Department.query.filter_by(id=student.department_id).first()
            print("DEPARTMENT:", department.department)
            student_data = {
                "id": student.id,
                "name": student.name,
                "student_number": student.student_number,
                "department_id": department.department,
                "mode_id": mode.mode
            }
            students_data.append(student_data)

        # Return the list of student dictionaries as JSON
        return jsonify(students=students_data)

@student_blp.route('/students/modeUodate',  methods=['PUT'])
class StudentMode(MethodView):

    @student_blp.arguments(StudentModesSchema)
    @student_blp.response(200, StudentModesSchema)
    def put(self,student_data):

        mode = Mode.query.filter_by(mode=student_data['modes']).first()

        #getting the student from the database
        if mode is None:
            abort(404, message="Mode not found")

        student = Student.query.filter_by(student_number=student_data['student_number']).first()
        if student is None:
            abort(404, message="Student not found")
        #getting the mode from the database
        
        
        print("Found student:", student.name)
        print("Found mode:", mode.mode)
        student = Student.query.filter_by(student_number=student_data['student_number']).first()
        student.mode_id = mode.id
        db.session.commit()
        
    
        
        student = Student.query.filter_by(student_number=student_data['student_number']).first()

        return {"message": f"Student mode updated successfully: {student.mode_id}"}, 201
        
@student_blp.route('/students/queue-start')
class StudentTicket(MethodView):
    @student_blp.arguments(TicketGenerateSchema)
    def post(self, student_data):
        # Fetch all students from the database
        try:
            student = Student.query.filter_by(student_number=student_data['student_number']).first()

            if not student:
                abort(404, message="Student not found")
            check = EnrollAssignment.query.filter_by(student_name_id=student.id).first()
            if check is not None:
                abort(409, message="Student already has a ticket")
            mode = Mode.query.filter_by(id=student.mode_id).first()
            if not mode:
                abort(404, message="Mode not found")
            sem = Sem.query.filter_by(id=1).first()
            if not sem:
                abort(404, message="Sem not found")
            #count all the student in the queue in enroll_assign_table WHERE status_id = 1 and department_id = student.department_id from EnrollAssignment table

            
            count = EnrollAssignment.query.filter_by(status_id=1, department_id=student.department_id).count()
            enroll_assignments = EnrollAssignment.query.all()
            count_id = len(enroll_assignments)


            print("COUNT:", count)
            if count is None:
                count = 0

            print(count)
            department = Department.query.filter_by(id=student.department_id).first()
            ticket_count = count + 1
            count_id = count_id + 1

            ticket_number = str(department.department) + str(mode.mode) + str(sem.id) + str(ticket_count)
            print(ticket_number)

            #get enroller with the same department and mode

            print(department.id)
            #filter enrollers by department and mode is done by the find_by_mode_and_department method in the Enroller model
            enrollers = Enroller.query.filter_by(assigned_mode_id=mode.id, department_id=department.id).first()
            print("MODE NEED:",mode.id)
            print("REQUIRED DEPARTMENT:",department.id)


            
            print(enrollers)
            if enrollers is None:
                abort(404, message=f"No assigned enroller yet to {department.department} in Mode: {mode.mode}")
            # print("ASSIGNED ENROLLER:", enroller.name,"TO:",student.name)
            
            # for enroller in enrollers:
            #     print(enroller.id)
            #     print(enroller.name)
            #     print(mode.id)
            #     print(enroller.department_id)

            

            # enrollers_data = []

            # for enroller in enrollers:
            #     if enroller.assigned_mode_id == mode.id:
            #         enroller_data = {
            #             "id": enroller.id,
            #             "name": enroller.name,
            #             "mode": mode.id,
            #             "department_id": enroller.department_id,
            #         }
            #         enrollers_data.append(enroller_data)
            

            db.session.add(TicketEnrollment(ticket_number=ticket_number, student_id=student.id))
            db.session.commit()          


        except SQLAlchemyError as e:
            abort(500, message=f"Internal server error: {e}")

        # enroller_data=enrollers_data[0]
        # print(enroller_data)

        print(".........................//////////......",enrollers)
        ticket = TicketEnrollment.query.filter_by(ticket_number=ticket_number).first()
        if not ticket:
            abort(404, message="Ticket not found")
        
        data = {
            "id":count_id,
            "student_name_id":student.id,
            "ticket_id":ticket.id,
            "department_id":department.id,
            "enroller_name_id":enrollers.id,
            #"enroller_name_id":enrollers_data["id"],
            "status_id":1
            }
            # Assuming status_id is 1 for now, change it as needed
        student_queue = EnrollAssignment(**data)
        db.session.add(student_queue)
        db.session.commit()

        

        # {
        #     "id": 19,
        #     "mode": "F2F",
        #     "name": "Ryan Wright",
        #     "student_number": "2012345696"
        # }  
        return {"message": "Ticket generated successfully", "ticket_number": ticket_number}
    
    def get(self):
        enrollees = EnrollAssignment.query.filter_by(status_id=1).all()
        enrollees_list = []

        # print(jsonify(queue_list))
        # for student in queue:
            
        #     student = Student.query.filter_by(id=student.student_name_id).first()
        #     enroller = Enroller.query.filter_by(enroller_name_id=student.id).first()
        #     ticket = TicketEnrollment.query.filter_by(id=student.ticket_id).first()
        #     mode = Mode.query.filter_by(id=student.mode_id).first()
        for enrollee in enrollees: 

            student = Student.query.filter_by(id=enrollee.student_name_id).first()
            mode = Mode.query.filter_by(id=student.mode_id).first()
            student_data = {
                "id": enrollee.id,
                "mode": mode.mode,
                "name": student.name,
                "student_number": student.student_number
            }
            enrollees_list.append(student_data)
        
        print(jsonify(enrollees_list))

        
        return jsonify(enrollees_list)

@student_blp.route('/students/queue-get-student/<student_num>')
class GetAllQueue(MethodView):

    def get(self,student_num):
        return{"Message":"Not yet implemented"}


@student_blp.route('/student_create')
class StudentCreateView(MethodView):

    @student_blp.arguments(StudentSchema)
    @student_blp.response(201, StudentSchema)
    def post(self,student_data):
        data = Student(**student_data)
        try:
            db.session.add(data)
            db.session.commit()
        except IntegrityError:
            abort(409, message="Student already exists")
        except SQLAlchemyError as e:
            abort(500, message=f"Internal server error: {e}")

        return {"message": "Student created successfully"}, 201


@student_blp.route('/student/<student_num>') #125:000:99/student/2021105252
class FindStudentNumber(MethodView):
    def get(self, student_num):
        print(student_num)
        student = Student.query.filter_by(student_number=student_num).first() #student_num is string
        
        if not student:
            abort(404, message="Student not found")

        student_department = Department.query.filter_by(id=student.department_id).first()
        print(student_department.department)
        
        return {"student_name": student.name, "student_number": student.student_number, "department": student_department.department}