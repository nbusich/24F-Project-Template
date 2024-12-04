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
@advisors.route('/createcompanychat/id', methods=['POST'])
def add_new_chat(id):
    
    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    
    query = f'''
        INSERT INTO chatroom (receiverID, senderID)
        SELECT
        advisor.id AS AdvisorID,
        company.id AS CompanyID
        FROM
        application
        JOIN
        student ON application.applicantID = student.id
        JOIN
        advisor ON student.advisorID = advisor.id
        JOIN
        jobListing ON application.listingID = jobListing.id
        JOIN
        company ON jobListing.companyID = company.id
        WHERE
        application.id = id;

    '''
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully added chat")
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Delete a chat 
@advisors.route('/deletechat/id', methods=['DELETE'])
def delete_chat(id):

    
    query = f'''
        DELETE FROM chatroom 
        WHERE
        sender.id = id;
    '''

    # executing and committing the delete statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully deleted chat")
    response.status_code = 200
    return response

#------------------------------------------------------------
# Update student info for student with particular ID
@advisors.route('/updateStudent', methods=['PUT'])
def update_student():
    current_app.logger.info('PUT /student route')
    stud_info = request.json
    stud_id = stud_info['id']
    stud_resume = stud_info['resume']

    query = 'UPDATE student SET resume = %s where id = %s'
    data = (stud_id, stud_resume)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'customer updated!'
