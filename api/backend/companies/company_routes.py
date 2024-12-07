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
    companyID = the_data['companyid']

    rel_majors = the_data['rel_majors']
    rel_fields = the_data['rel_fields']
    
    query = f'''
        INSERT IGNORE INTO jobListing (title,
                              description,
                              numApplicants, 
                              payPerHour,
                              applicationDeadline,
                              numOpenings,
                              requiredGPA,
                              companyID)
        VALUES ('{title}', '{description}', {str(applicants)}, 
        {str(pay)}, '{deadline}', {str(openings)}, {str(gpa)}, {str(companyID)})
    '''

    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    # Now retrieve the last inserted ID
    job_listing_id = cursor.lastrowid

    for major in rel_majors:
        query = f'''
            INSERT INTO relevantMajors (listingID, major)
            VALUES ('{job_listing_id}', '{major}')
        '''
        current_app.logger.info(query)

        # executing and committing the insert statement 
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
    
    for field in rel_fields:
        query = f'''
            INSERT INTO relevantFields (listingID, field)
            VALUES ('{job_listing_id}', '{field}')
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
@companies.route('/jobListing/<listingID>', methods=['GET'])
def view_joblisting (listingID):
    
    query = f'''
        SELECT title, company.name AS 'companyName', description, jobListing.id, company.id, numApplicants, payPerHour, applicationDeadline, numOpenings, requiredGPA, acceptanceRate
        FROM jobListing JOIN company
            ON jobListing.companyID = company.id
        WHERE jobListing.id = {str(listingID)}
    '''

    # logging the query for debugging purposes.  
    # The output will appear in the Docker logs output
    # This line has nothing to do with actually executing the query...
    # It is only for debugging purposes. 
    current_app.logger.info(f'GET /jobListing/<listingID> query={query}')

    # get the database connection, execute the query, and 
    # fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    # Another example of logging for debugging purposes.
    # You can see if the data you're getting back is what you expect. 
    current_app.logger.info(f'GET /jobListing/<listingID> Result of query = {theData}')
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


# ------------------------------------------------------------
# This is a GET route for all job listings.
@companies.route('/jobListing', methods=['GET'])
def access_all_joblistings ():
    
    query = f'''
        SELECT title, company.name AS 'companyName', 
        description, numApplicants, payPerHour, applicationDeadline, numOpenings, requiredGPA, jobListing.id, company.id, acceptanceRate
        FROM jobListing JOIN company
            ON jobListing.companyID = company.id
        ORDER BY jobListing.id DESC
    '''

    # logging the query for debugging purposes.  
    # The output will appear in the Docker logs output
    # This line has nothing to do with actually executing the query...
    # It is only for debugging purposes. 
    current_app.logger.info(f'GET /jobListing query={query}')

    # get the database connection, execute the query, and 
    # fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    # Another example of logging for debugging purposes.
    # You can see if the data you're getting back is what you expect. 
    current_app.logger.info(f'GET /jobListing Result of query = {theData}')
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


# ------------------------------------------------------------
# This is a GET route for all relevant majors of a particular job listing.
@companies.route('/relevantMajors/<listingID>', methods=['GET'])
def get_majors (listingID):
    
    query = f'''
        SELECT DISTINCT major
        FROM relevantMajors JOIN jobListing
            ON relevantMajors.listingID = {str(listingID)}
    '''

    # logging the query for debugging purposes.  
    # The output will appear in the Docker logs output
    # This line has nothing to do with actually executing the query...
    # It is only for debugging purposes. 
    current_app.logger.info(f'GET /relevantMajors/<listingID> query={query}')

    # get the database connection, execute the query, and 
    # fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    # Another example of logging for debugging purposes.
    # You can see if the data you're getting back is what you expect. 
    current_app.logger.info(f'GET /relevantMajors/<listingID> Result of query = {theData}')
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response



# ------------------------------------------------------------
# This is a GET route for all relevant fields of a particular job listing.
@companies.route('/relevantFields/<listingID>', methods=['GET'])
def get_fields (listingID):
    
    query = f'''
        SELECT DISTINCT field
        FROM relevantFields JOIN jobListing
            ON relevantFields.listingID = {str(listingID)}
    '''

    # logging the query for debugging purposes.  
    # The output will appear in the Docker logs output
    # This line has nothing to do with actually executing the query...
    # It is only for debugging purposes. 
    current_app.logger.info(f'GET /relevantFields/<listingID> query={query}')

    # get the database connection, execute the query, and 
    # fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    # Another example of logging for debugging purposes.
    # You can see if the data you're getting back is what you expect. 
    current_app.logger.info(f'GET /relevantFields/<listingID> Result of query = {theData}')
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response





# ------------------------------------------------------------
# This is a GET route for all job listings of a particular company.
@companies.route('/myJobListing/<companyID>', methods=['GET'])
def access_company_joblistings (companyID):
    
    query = f'''
        SELECT DISTINCT title, description, jobListing.id AS listingID, numApplicants, payPerHour, 
        applicationDeadline, numOpenings, requiredGPA, jobListing.companyID AS lcid, company.id AS cid
        FROM jobListing JOIN company
            ON company.id = {str(companyID)}
                AND company.id = jobListing.companyID

        ORDER BY jobListing.id DESC
    '''

    # logging the query for debugging purposes.  
    # The output will appear in the Docker logs output
    # This line has nothing to do with actually executing the query...
    # It is only for debugging purposes. 
    current_app.logger.info(f'GET /myJobListing/<companyID> query={query}')

    # get the database connection, execute the query, and 
    # fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    # Another example of logging for debugging purposes.
    # You can see if the data you're getting back is what you expect. 
    current_app.logger.info(f'GET /myJobListing/<companyID> Result of query = {theData}')
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response




# ------------------------------------------------------------
# This is a PUT route to update an existing job listing.
@companies.route('/jobListing/<listingID>', methods=['PUT'])
def update_joblisting(listingID):
    
    # In a PUT request, there is a 
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

    new_majors = the_data['new_majors']
    new_fields = the_data['new_fields']

    dropped_majors = the_data['dropped_majors']
    dropped_fields = the_data['dropped_fields']
    
    query = f'''
        UPDATE jobListing
        SET title = '{title}',
            description = '{description}',
            numApplicants = {str(applicants)}, 
            payPerHour = {str(pay)},
            numOpenings = {str(openings)},
            requiredGPA = {str(gpa)}
        WHERE id = {str(listingID)}
    '''

    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    for major in new_majors:
        query = f'''
            INSERT IGNORE INTO relevantMajors (listingID, major)
            VALUES ({str(listingID)}, '{major}')
        '''
        current_app.logger.info(query)

        # executing and committing the insert statement 
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
    
    for field in new_fields:
        query = f'''
            INSERT IGNORE INTO relevantFields (listingID, field)
            VALUES ({str(listingID)}, '{field}')
        '''
        current_app.logger.info(query)

        # executing and committing the insert statement 
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
    

    for major in dropped_majors:
        query = f'''
            DELETE FROM relevantMajors WHERE (listingID = {str(listingID)} AND major = '{major}')
        '''
        current_app.logger.info(query)

        # executing and committing the insert statement 
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
    
    for field in dropped_fields:
        query = f'''
            DELETE FROM relevantFields WHERE (listingID = {str(listingID)} AND field = '{field}')
        '''
        current_app.logger.info(query)

        # executing and committing the insert statement 
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()

    response = make_response("Successfully updated job listing")
    response.status_code = 200
    return response


# ------------------------------------------------------------
# This is a GET route for all unique relevant majors in the db
@companies.route('/relevantMajors', methods=['GET'])
def all_majors ():
    
    query = f'''
        SELECT DISTINCT major
        FROM relevantMajors
        ORDER BY major ASC
    '''

    # logging the query for debugging purposes.  
    # The output will appear in the Docker logs output
    # This line has nothing to do with actually executing the query...
    # It is only for debugging purposes. 
    current_app.logger.info(f'GET /relevantMajors query={query}')

    # get the database connection, execute the query, and 
    # fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    # Another example of logging for debugging purposes.
    # You can see if the data you're getting back is what you expect. 
    current_app.logger.info(f'GET /relevantMajors Result of query = {theData}')
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


# ------------------------------------------------------------
# This is a GET route for all unique relevant fields in the db
@companies.route('/relevantFields', methods=['GET'])
def all_fields ():
    
    query = f'''
        SELECT DISTINCT field
        FROM relevantFields
        ORDER BY field ASC
    '''

    # logging the query for debugging purposes.  
    # The output will appear in the Docker logs output
    # This line has nothing to do with actually executing the query...
    # It is only for debugging purposes. 
    current_app.logger.info(f'GET /relevantFields query={query}')

    # get the database connection, execute the query, and 
    # fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    # Another example of logging for debugging purposes.
    # You can see if the data you're getting back is what you expect. 
    current_app.logger.info(f'GET /relevantFields Result of query = {theData}')
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
# This is a GET route for the user's company
@companies.route('/myCompany/<compID>', methods=['GET'])
def mycompany (compID):

    query = f'''
        SELECT name
        FROM company
        WHERE company.id = {str(compID)}
    '''

    # logging the query for debugging purposes.  
    # The output will appear in the Docker logs output
    # This line has nothing to do with actually executing the query...
    # It is only for debugging purposes. 
    current_app.logger.info(f'GET /myCompany query={query}')

    # get the database connection, execute the query, and 
    # fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    # Another example of logging for debugging purposes.
    # You can see if the data you're getting back is what you expect. 
    current_app.logger.info(f'GET /myCompany Result of query = {theData}')
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response



# ------------------------------------------------------------
# This is a DELETE route for a particular job listing.
@companies.route('/jobListing/<listingID>', methods=['DELETE'])
def delete_joblisting (listingID):
    
    query = f'''
        DELETE FROM jobListing 
        WHERE jobListing.id = {str(listingID)}
    '''

    # logging the query for debugging purposes.  
    # The output will appear in the Docker logs output
    # This line has nothing to do with actually executing the query...
    # It is only for debugging purposes. 
    current_app.logger.info(f'DELETE /jobListing/<listingID> query={query}')

    # get the database connection, execute the query, and 
    # fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    affected_rows = cursor.rowcount  # Returns the number of rows affected

    if affected_rows > 0:
        current_app.logger.info(f'Deleted {affected_rows} job listing(s) with ID {listingID}')
    else:
        current_app.logger.warning(f'No job listing found with ID {listingID}')
    
    # Another example of logging for debugging purposes.
    # You can see if the data you're getting back is what you expect. 
    
    response_data = {
    "message": "Job listing deleted successfully." if affected_rows > 0 else "Job listing not found."
    }
    response = make_response(jsonify(response_data))
    response.status_code = 200 if affected_rows > 0 else 404  # 404 for not found

    return response
