from db import db
from datetime import datetime

class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey(
        'course.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey(
        'students.id'), nullable=False)
    grades = db.Column(db.String(255))
    grade_points = db.Column(db.Float)

    def calculate_grade_points(self):
        grade_map = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0}
        grade_tokens = self.grades.split(',')
        grade_values = []
        for token in grade_tokens:
            token = token.strip()
            if token in grade_map:
                grade_values.append(grade_map[token])
            else:
                raise ValueError(f"Grade {token} not recognized.")
        self.grade_points = sum(grade_values) / len(grade_values)




class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    teacher = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    enrollments = db.relationship('Enrollment', backref='course', lazy=True)




class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    enrollments = db.relationship('Enrollment', backref='student', lazy=True)

    @property
    def gpa(self):
        # Calculate the student's GPA based on their grades in each course
        # We assume that each enrollment has a grade_points field
        enrollments = Enrollment.query.filter_by(student_id=self.id).all()
        if len(enrollments) == 0:
            return None
        total_points = sum(
            [enrollment.grade_points for enrollment in enrollments])
        gpa = total_points
        return gpa / len(enrollments)

