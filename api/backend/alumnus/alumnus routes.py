########################################################
# Sample alumnus blueprint of endpoints
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
alumnus = Blueprint('alumnus', __name__)


#------------------------------------------------------------
# gets a list of students in a specific major
@alumnus.route('/student/<major>', methods=['GET'])
def get_students_in_major(major):

    query = '''
    SELECT id, firstName, lastName,
             FROM student
             WHERE student.major = major;

    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)

    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------


#------------------------------------------------------------
# updates a job from a user given their id, probably
@alumnus.route('/alumnus/<id>', methods=['PUT'])
def update_alumni_job(id):

    alumn_info = request.json
    alumn_id = alumn_info['id']
    alumn_job = alumn_info['jobID']

    query = '''
    UPDATE alumnus
    SET jobID = %s
    WHERE id = id;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, alumn_info)
    db.get_db().commit()
    response = make_response("job updated")!
    response.status_code = 200
    return response

#------------------------------------------------------------
# creates a new chat with a student, hopefully
@alumnus.route('/chatroom/<userID>', methods=['POST'])
def create_new_chat(id):

    data = request.json
    student_id = data['userID']

    query = '''
    INSERT INTO chatroom (recieverID, senderID) VALUES (%s, %s);
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (student_id, id))
    db.get_db().commit()
    response = make_response("chat created!")!
    response.status_code = 200
    return response


# ------------------------------------------------------------
# Deletes a chat 
@alumnus.route('/chatroom/<senderID>', methods=['DELETE'])
def delete_chat(id):

    query = '''
        DELETE FROM chatroom 
        WHERE
        sender.id = id;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("chat deleted!")
    response.status_code = 200
    return response

