from flask.views import MethodView
from flask_smorest import Blueprint,abort #blueprint is used to register informations in the StudentBlueprint

from db import db
from Schemas import CourseSchema, StudentSchema
from sqlalchemy.exc import SQLAlchemyError
from models import models


CourseBlueprint =  Blueprint("course", __name__, description="Operations on Courses")


@CourseBlueprint.route('/courses')
class CoursesView(MethodView):
    @CourseBlueprint.response(200, CourseSchema(many=True))

    def get(self):
        """Get all courses"""
        courses = Course.query.all()
        return courses

    @CourseBlueprint.arguments(CourseSchema)
    @CourseBlueprint.response(201, CourseSchema)

    def post(self, course):
        """Create a new course"""
        db.session.add(course)
        db.session.commit()
        return course


@CourseBlueprint.route('/courses/int:id')
class CourseView(MethodView):
    @CourseBlueprint.response(200, CourseSchema)

    def get(self, id):
        """Get a course by ID"""
        course = Course.query.get_or_404(id)
        return course

    @CourseBlueprint.arguments(CourseSchema)
    @CourseBlueprint.response(200, CourseSchema)
  
    def put(self, course, id):
        """Update a course by ID"""
        old_course = Course.query.get_or_404(id)
        old_course.name = course.name
        old_course.teacher = course.teacher
        db.session.commit()
        return old_course

    @CourseBlueprint.response(200)
   
    def delete(self, id):
        """Delete a course by ID"""
        course = Course.query.get_or_404(id)
        db.session.delete(course)
        db.session.commit()
        return course

@CourseBlueprint.route('/courses/int:id/students')
class CourseStudentsView(MethodView):
    @CourseBlueprint.response(200)
    
    def get(self, id):
        """Get all students registered in a course"""
        course = Course.query.get_or_404(id)
        students = [enrollment.student for enrollment in course.enrollments]
        return students