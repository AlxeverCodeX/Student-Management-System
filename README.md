# Student-Management-System

This project is a RESTful API built using Flask-Smorest frameworks in Python. The API provides functionality for creating, reading, updating, and deleting students as well as registering courses. It also allows retrieving all the students, all the courses, and all the students registered in a particular course, and retrieving the grades for each student in each course. It calculates the GPA for each student based on their grades in each course.

This  API was built with Python's flask-smorest as part of Backend Engineering (Python) Third Semester Examination Project at [Altschool Africa](https://www.altschoolafrica.com/)



# Built With:
![Python](https://img.shields.io/badge/-Python-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/-Flask-black?logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/-SQLite-blue?logo=sqlite&logoColor=white)


# Installation

1. Clone the repository to your local machine
`git clone https://github.com/AlxeverCodeX/https://github.com/AlxeverCodeX/Student-Management-System.git`

2. Install the required packages using pip.
`pip install -r requirements.txt`

3. Start the Flask application.
`flask run`

 The application will be available at http://localhost:5000.

# Usage

The API supports the following endpoints:

GET /students: Retrieves all students in the database.

GET /students/{id}: Retrieves a specific student by ID.

POST /students: Creates a new student.

PUT /students/{id}: Updates an existing student by ID.

DELETE /students/{id}: Deletes a student by ID.

GET /courses: Retrieves all courses in the database.

GET /courses/{id}: Retrieves a specific course by ID.

POST /courses: Creates a new course.

PUT /courses/{id}: Updates an existing course by ID.

DELETE /courses/{id}: Deletes a course by ID.

GET /courses/{id}/students: Retrieves all the students registered in a particular course.

GET /students/{id}/courses: Retrieves all the courses that a particular student is registered for.

GET /students/{id}/grades: Retrieves the grades for a particular student in all the courses they are registered for.

GET /courses/{id}/grades: Retrieves the grades for all the students registered in a particular course.



## Contact

Emmanuel Albert - [@alnuelCode_X](https://twitter.com/alnuelCode_X) - salberthp89@gmail.com

Project Link: [Student-Management-System](https://github.com/AlxeverCodeX/Student-Management-System)


## License

Distributed under the MIT License. See <a href="https://github.com/AlxeverCodeX/Student-Management-System/blob/main/LICENSE">LICENSE</a> for more information.


## Acknowledgements

This project was made possible by:

* [AltSchool Africa School of Engineering](https://altschoolafrica.com/schools/engineering)
* [Caleb Emelike's Flask Lessons](https://github.com/CalebEmelike)

