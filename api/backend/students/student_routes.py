########################################################
# Student Routes
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
students = Blueprint('students', __name__)


# ------------------------------------------------------------
# This is POST route to add a new student.
@students.route('/students', methods=['POST'])
def add_student():
    the_data = request.json
    current_app.logger.info(the_data)

    name = the_data['name']
    email = the_data['email']
    major = the_data['major']
    graduation_year = the_data['graduation_year']

    query = f'''
        INSERT INTO Student (name, email, major, graduation_year)
        VALUES ('{name}', '{email}', '{major}', {graduation_year})
    '''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Student added successfully", 200)
    return response

# ------------------------------------------------------------
# This is a GET route for a specific student by ID.
@students.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    query = f'''
        SELECT id, name, email, major, graduation_year
        FROM Student
        WHERE id = {student_id}
    '''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_data = cursor.fetchall()

    response = make_response(jsonify(the_data), 200)
    return response

# ------------------------------------------------------------
# This is a GET route for all students.
@students.route('/students', methods=['GET'])
def get_all_students():
    query = '''
        SELECT id, name, email, major, graduation_year
        FROM Student
        ORDER BY id ASC
    '''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_data = cursor.fetchall()

    response = make_response(jsonify(the_data), 200)
    return response

# ------------------------------------------------------------
# This is a PUT Route for specific students.
@students.route('/students/<student_id>', methods=['PUT'])
def update_student(student_id):
    the_data = request.json
    current_app.logger.info(the_data)

    name = the_data.get('name')
    email = the_data.get('email')
    major = the_data.get('major')
    graduation_year = the_data.get('graduation_year')

    query = f'''
        UPDATE Student
        SET name = '{name}', email = '{email}', major = '{major}', graduation_year = {graduation_year}
        WHERE id = {student_id}
    '''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Student updated successfully", 200)
    return response

# ------------------------------------------------------------
# This is DELETE route for specific students.
@students.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    query = f'''
        DELETE FROM Student
        WHERE id = {student_id}
    '''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Student deleted successfully", 200)
    return response