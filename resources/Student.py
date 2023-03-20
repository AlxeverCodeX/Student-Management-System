from flask.views import MethodView
from flask_smorest import Blueprint,abort #blueprint is used to register informations in the StudentBlueprint
from db import db
from Schemas import StudentSchema, EnrollmentSchema
from sqlalchemy.exc import SQLAlchemyError
from models import models, Student


StudentBlueprint =  Blueprint("student", __name__, description="Operations on students")




@StudentBlueprint.route('/students')
class StudentsView(MethodView):
    @StudentBlueprint.response(200, StudentSchema(many=True))
 
    def get(self):
        """Get all students"""
        students = Student.query.all()
        return students

    @StudentBlueprint.arguments(StudentSchema)
    @StudentBlueprint.response(201, StudentSchema)

    def post(self, student):
        """Create a new student"""
        student = Student(**student)
        db.session.add(student)
        db.session.commit()
        return student


@StudentBlueprint.route('/students/<int:id>')
class StudentView(MethodView):
    @StudentBlueprint.response(200, StudentSchema)

    def get(self, id):
        """Get a student by ID"""
        student = Student.query.get_or_404(id)
        return student

    @StudentBlueprint.arguments(StudentSchema)
    @StudentBlueprint.response(200, StudentSchema)
 
    def put(self, student, id):
        """Update a student by ID"""
        old_student = Student.query.get_or_404(id)
        old_student.name = student['name']
        old_student.email = student['email']
        db.session.commit()
        return old_student

    @StudentBlueprint.response(204)
  
    def delete(self, id):
        """Delete a student by ID"""
        student = Student.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        return ''


@StudentBlueprint.route('/students/<int:id>/enrollments')
class StudentEnrollmentsView(MethodView):
    @StudentBlueprint.response(200, EnrollmentSchema(many=True))

    def get(self, id):
        """Get all enrollments for a student"""
        student = Student.query.get_or_404(id)
        enrollments = student.enrollments
        return enrollments

"""
@StudentBlueprint.route('/students/int:id/gpa')
class StudentGPAView(MethodView):
    @StudentBlueprint.response(GPASchema)
    @jwt_required()
    def get(self, id):
        #Get the GPA for a student
        student = Student.query.get_or_404(id)
        gpa = student.calculate_gpa()
        return {'gpa': gpa}
        
"""
