########################################################
# Advisor Routes
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
advisors = Blueprint('advisors', __name__)


#------------------------------------------------------------
# Get statistics about job applications
@advisors.route('/jobListingData', methods=['GET'])
def get_applicationstats():

    cursor = db.get_db().cursor()
    cursor.execute('''
                   SELECT 
                   jobListing.title AS PositionTitle,
                   company.name AS CompanyName,
                   AVG(jobListing.payPerHour) AS AvgPayPerHour,
                   COUNT(application.listingID) AS TotalApplications,
                   COUNT(application.listingID) / jobListing.numOpenings AS AcceptanceRate
                   FROM 
                   jobListing
                   JOIN 
                   company ON jobListing.companyID = company.id
                   LEFT JOIN 
                   application ON jobListing.id = application.listingID
                   GROUP BY 
                   jobListing.id, company.name;
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get co-ops that the student can apply to based on their gpa and deadline to submit
@advisors.route('/studentRecs/<id>', methods=['GET'])
def get_rel_coops(id):
    cursor = db.get_db().cursor()
    cursor.execute('''
                   SELECT 
                   student.firstName, 
                   student.lastName, 
                   jobListing.title AS JobTitle, 
                   jobListing.description AS JobDescription, 
                   jobListing.requiredGPA, 
                   student.gpa
                   FROM student
                   JOIN 
                   jobListing ON student.gpa >= jobListing.requiredGPA
                   WHERE 
                   student.id = %s;
    ''', (id,))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get students with the same major as given student
@advisors.route('/studentConnect/<id>', methods=['GET'])
def get_students_same_major(id):
    cursor = db.get_db().cursor()
    cursor.execute('''
                   SELECT 
                   s1.firstName AS StudentFirstName,
                   s1.lastName AS StudentLastName,
                   s1.major AS Major,
                   s2.firstName AS PeerFirstName,
                   s2.lastName AS PeerLastName
                   FROM 
                   student AS s1
                   JOIN 
                   student AS s2 ON s1.major = s2.major AND s1.id != s2.id
                   WHERE 
                   s1.id = %s;
    ''', (id,))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get students that have worked in a specified company
@advisors.route('/studentAtCompany/<id>', methods=['GET'])
def get_rel_students(id):
    cursor = db.get_db().cursor()
    cursor.execute('''
                   SELECT 
                   s.firstName, s.lastName, p.comment
                   FROM student s
                   JOIN position p ON s.pastPositionID = p.id
                   JOIN company c ON p.companyID = c.id
                   WHERE 
                   c.id = %s;
    ''', (id,))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get student information from a certain application
@advisors.route('/applicationInfo/<id>', methods=['GET'])
def get_students_app_info(id):
    cursor = db.get_db().cursor()
    cursor.execute('''
                   SELECT
                   student.firstName,
                   student.lastName,
                   student.resume,
                   student.major,
                   application.coverLetter,
                   jobListing.title AS JobTitle,
                   jobListing.description AS JobDescription
                   FROM
                   student
                   JOIN
                   application ON student.id = application.applicantID
                   JOIN
                   jobListing ON application.listingID = jobListing.id
                   WHERE
                   application.id = %s;
    ''', (id,))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# ------------------------------------------------------------
# Create a chatroom between advisor and a company from a certain application
@advisors.route('/createcompanychat/<adv_id>/<comp_id>', methods=['POST'])
def add_new_chat(adv_id, comp_id):
    try:
        # Log the incoming IDs for debugging
        current_app.logger.info(f"Advisor ID: {adv_id}, Company ID: {comp_id}")

        # Validate that the advisor and company exist
        validation_query = '''
            SELECT EXISTS(SELECT 1 FROM advisor WHERE id = %s) AS advisor_exists,
                   EXISTS(SELECT 1 FROM company WHERE id = %s) AS company_exists
        '''
        cursor = db.get_db().cursor()
        cursor.execute(validation_query, (adv_id, comp_id))
        validation_result = cursor.fetchone()

        if not validation_result or not validation_result['advisor_exists'] or not validation_result['company_exists']:
            response = make_response("Invalid advisor or company ID.")
            response.status_code = 400
            return response

        # Insert a new chatroom
        insert_query = '''
            INSERT INTO chatroom (receiverID, senderID)
            VALUES (%s, %s)
        '''
        cursor.execute(insert_query, (adv_id, comp_id))
        db.get_db().commit()

        response = make_response("Successfully added chat")
        response.status_code = 200
        return response

    except Exception as e:
        db.get_db().rollback()
        current_app.logger.error(f"Error creating chatroom: {e}")
        response = make_response(f"Error creating chatroom: {str(e)}")
        response.status_code = 500
        return response

# ------------------------------------------------------------
# Delete a chat 
@advisors.route('/deletechat/<adv_id>/<comp_id>', methods=['DELETE'])
def delete_chat(adv_id, comp_id):
    try:
        # Log the incoming IDs for debugging
        current_app.logger.info(f"Advisor ID: {adv_id}, Company ID: {comp_id}")

        # Confirm the chatroom exists
        validation_query = '''
            SELECT EXISTS(
                SELECT 1 FROM chatroom 
                WHERE receiverID = %s AND senderID = %s
            ) AS chatroom_exists
        '''
        cursor = db.get_db().cursor()
        cursor.execute(validation_query, (adv_id, comp_id))
        validation_result = cursor.fetchone()

        if not validation_result or not validation_result['chatroom_exists']:
            response = make_response("Chatroom not found.")
            response.status_code = 404
            return response

        # Delete the chatroom
        delete_query = '''
            DELETE FROM chatroom 
            WHERE receiverID = %s AND senderID = %s
        '''
        cursor.execute(delete_query, (adv_id, comp_id))
        db.get_db().commit()

        # Confirm deletion
        if cursor.rowcount > 0:
            response = make_response("Successfully deleted chat")
            response.status_code = 200
        else:
            response = make_response("Failed to delete chat.")
            response.status_code = 400
        return response

    except Exception as e:
        db.get_db().rollback()
        current_app.logger.error(f"Error deleting chatroom: {e}")
        response = make_response(f"Error deleting chatroom: {str(e)}")
        response.status_code = 500
        return response

#------------------------------------------------------------
# Update student info for student with particular ID
@advisors.route('/updateStudent', methods=['PUT'])
def update_student():
    current_app.logger.info('PUT /updateStudent route')

    stud_info = request.json
    student_id = stud_info['student_id']
    advisor_id = stud_info['advisor_id']
    resume = stud_info['resume']

    query = 'UPDATE student SET advisorID = %s, resume = %s WHERE id = %s'
    data = (advisor_id, resume, student_id)

    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, data)
        db.get_db().commit()

        if cursor.rowcount > 0:
            response = make_response("Successfully updated student")
            response.status_code = 200
        else:
            response = make_response("No rows updated, check the ID")
            response.status_code = 404
    except Exception as e:
        db.get_db().rollback()
        current_app.logger.error(f"Error updating student: {str(e)}", exc_info=True)
        response = make_response(f"Error updating student: {str(e)}")
        response.status_code = 500

    return response

