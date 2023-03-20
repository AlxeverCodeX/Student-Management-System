from flask.views import MethodView
from flask_smorest import Blueprint,abort #blueprint is used to register informations in the StudentBlueprint
from flask import request
from db import db
from Schemas import EnrollmentSchema
from sqlalchemy.exc import SQLAlchemyError
from models import Enrollment


EnrollmentBlueprint =  Blueprint("enrollment", __name__, description="Operations on student enrollment")



@EnrollmentBlueprint.route('/enrollments')
class EnrollmentsView(MethodView):
    @EnrollmentBlueprint.response(200, EnrollmentSchema(many=True))
    
    def get(self):
        """Get all enrollments"""
        enrollments = Enrollment.query.all()
        return enrollments


    @EnrollmentBlueprint.arguments(EnrollmentSchema)
    @EnrollmentBlueprint.response(200, EnrollmentSchema)
    
    def post(self, enrollment):
        """Create a new enrollment"""
        enrollments = Enrollment(**enrollment)
        db.session.add(enrollments)
        db.session.commit()
        return enrollments


@EnrollmentBlueprint.route('/enrollments/<int:id>')
class EnrollmentView(MethodView):
    @EnrollmentBlueprint.response(200, EnrollmentSchema)
    
    def get(self, id):
        """Get an enrollment by ID"""
        enrollment = Enrollment.query.get_or_404(id)
        return enrollment


    @EnrollmentBlueprint.arguments(EnrollmentSchema)
    @EnrollmentBlueprint.response(200, EnrollmentSchema)
   
    def put(self, enrollment, id):
        """Update an enrollment by ID"""
        enrollment = Enrollment.query.get_or_404(id)
        enrollment_data = request.json
        enrollment.course_id = enrollment_data.get('course_id', enrollment.course_id)
        enrollment.student_id = enrollment_data.get('student_id', enrollment.student_id)
        enrollment.grades = enrollment_data.get('grades', enrollment.grades)
        enrollment.calculate_grade_points()
        db.session.commit()
        return enrollment


    @EnrollmentBlueprint.response(201, EnrollmentSchema)

    def delete(self, id):
        """Delete an enrollment by ID"""
        enrollment = Enrollment.query.get_or_404(id)
        db.session.delete(enrollment)
        db.session.commit()
        return enrollment
