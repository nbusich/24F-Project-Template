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
    try:
        query = '''
            SELECT id, name, email, major, graduation_year
            FROM Student
            WHERE id = %s
        '''
        current_app.logger.info(f"Querying database for student ID: {student_id}")

        cursor = db.get_db().cursor()
        cursor.execute(query, (student_id,))
        result = cursor.fetchone()

        if not result:
            return jsonify({"error": f"Student with ID {student_id} not found"}), 404

        student_data = {
            "id": result[0],
            "name": result[1],
            "email": result[2],
            "major": result[3],
            "graduation_year": result[4]
        }

        return jsonify(student_data), 200

    except Exception as e:
        # Log the error and return a server error response
        current_app.logger.error(f"Error fetching student data: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

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
# This is a DELETE route for specific students.
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

# ------------------------------------------------------------
# This is a GET route for specific students.
@students.route('/students/<studentid>/coop_jobs', methods=['GET'])
def get_coop_jobs(student_id):
    # Query to find the student's major using their unique ID
    query_student = f'''
        SELECT major 
        FROM Student 
        WHERE id = {student_id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query_student)
    student_major = cursor.fetchone()  # Fetch one record (tuple)

    if not student_major:
        return make_response("Student not found", 404)
    
    major = student_major[0]
    
    query_jobs = f'''
        SELECT jl.title, jl.description, jl.numOpenings, jl.payPerHour, jl.companyID
        FROM jobListing jl
        JOIN relevantMajors rm ON jl.id = rm.listingID
        WHERE rm.major = '{major}'
    '''
    cursor.execute(query_jobs)
    jobs_data = cursor.fetchall()

    response = [
        {
            "title": job[0],
            "description": job[1],
            "numOpenings": job[2],
            "payPerHour": job[3],
            "companyID": job[4]
        } 
        for job in jobs_data
    ]
    return make_response(jsonify(response), 200)