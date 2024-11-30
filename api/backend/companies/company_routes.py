########################################################
# Company Routes
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
companies = Blueprint('companies', __name__)


# ------------------------------------------------------------
# This is a POST route to add a new job listing.
# Remember, we are using POST routes to create new entries
# in the database. 
@companies.route('/jobListing', methods=['POST'])
def add_new_joblisting():
    
    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    title = the_data['listing_title']
    description = the_data['listing_description']
    applicants = the_data['number_of_applicants']
    pay = the_data['listing_pay']
    deadline = the_data['listing_deadline']
    openings = the_data['listing_openings']
    gpa = the_data['listing_req_gpa']
    
    query = f'''
        INSERT INTO jobListing (title,
                              description,
                              numApplicants, 
                              payPerHour,
                              applicationDeadline,
                              numOpenings,
                              requiredGPA)
        VALUES ('{title}', '{description}', {str(applicants)}, 
        {str(pay)}, {str(deadline)}, {str(openings)}, {str(gpa)})
    '''

    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully added job listing")
    response.status_code = 200
    return response


# ------------------------------------------------------------
# This is a GET route for a particular job listing.
@companies.route('/jobListing/<id>', methods=['GET'])
def view_joblisting (id):
    
    query = f'''
        SELECT title, description, numApplicants, payPerHour, applicationDeadline, numOpenings, requiredGPA
        FROM jobListing
        WHERE listingID = {str(id)}

    '''

    # logging the query for debugging purposes.  
    # The output will appear in the Docker logs output
    # This line has nothing to do with actually executing the query...
    # It is only for debugging purposes. 
    current_app.logger.info(f'GET /jobListing/<id> query={query}')

    # get the database connection, execute the query, and 
    # fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    # Another example of logging for debugging purposes.
    # You can see if the data you're getting back is what you expect. 
    current_app.logger.info(f'GET /jobListing/<id> Result of query = {theData}')
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
