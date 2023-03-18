from flask.views import MethodView
from flask_smorest import Blueprint,abort #blueprint is used to register informations in the StudentBlueprint

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
        db.session.add(enrollment)
        db.session.commit()
        return enrollment


@EnrollmentBlueprint.route('/enrollments/int:id')
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
        old_enrollment = Enrollment.query.get_or_404(id)
        old_enrollment.course_id = enrollment.course_id
        old_enrollment.student_id = enrollment.student_id
        old_enrollment.grades = enrollment.grades
        old_enrollment.calculate_grade_points()
        db.session.commit()
        return old_enrollment


    @EnrollmentBlueprint.response(201, EnrollmentSchema)

    def delete(self, id):
        """Delete an enrollment by ID"""
        enrollment = Enrollment.query.get_or_404(id)
        db.session.delete(enrollment)
        db.session.commit()
        return enrollment
