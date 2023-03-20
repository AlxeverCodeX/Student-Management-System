from flask import Flask
from datetime import datetime
from resources.Student import StudentBlueprint
from resources.Course import CourseBlueprint
from resources.Enrollement import EnrollmentBlueprint
from db import db
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate
from flask_smorest import Api, Blueprint

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "STUDENT MANAGEMENT API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  

db.init_app(app)
api = Api(app)

api.register_blueprint(StudentBlueprint) 
api.register_blueprint(CourseBlueprint)
api.register_blueprint(EnrollmentBlueprint)




# Create the tables
with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(debug=True)







