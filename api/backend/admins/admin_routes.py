from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from datetime import datetime

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
admins = Blueprint('admins', __name__)
#------------------------------------------------------------
# Gets system status for queries, uptime, and cursers
@admins.route('/dashboard', methods=['GET'])
def get_dashboard():

    cursor = db.get_db().cursor()
    cursor.execute('''SHOW STATUS WHERE Variable_name IN ('Queries');''')
    
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Update change info for change with particular changeID
@admins.route('/changelog/<changeID>', methods=['PUT'])
def update_change(changeID):
    current_app.logger.info('PUT /changelog/<changeID> route')
    change_info = request.json
    description = change_info['description']
    changerID = change_info['changerID']

    query = 'UPDATE changes SET description = %s, changerID = %s WHERE id = %s'
    data = (description, changerID, changeID)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'change updated!'

#------------------------------------------------------------
# Gets the changelog's most recent changes
import logging
logging.basicConfig(level=logging.DEBUG)


@admins.route('/changelog', methods=['GET'])
def get_changes():
    cursor = db.get_db().cursor()

    # Debugging the query execution
    query = '''
        SELECT c.description, c.lastChange, a.firstname, a.lastname
        FROM changes c
        JOIN administrator a ON c.changerID = a.id
        ORDER BY lastChange DESC
        LIMIT 10;
    '''

    logging.debug(f"Executing query: {query}")
    cursor.execute(query)

    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200

    logging.debug(f"Fetched rows: {theData}")  # Inspect the rows returned

    cursor.execute('SELECT DATABASE();')
    db_name = cursor.fetchone()
    logging.debug(f"Connected to database: {db_name}")

    return response


#------------------------------------------------------------
# Creates a change in the changelog
@admins.route('/changelog/<changerid>', methods=['POST'])
def add_new_change(changerid):
    # In a POST request, there is a
    # collecting data from the request object
    the_data = request.json
    description = the_data.get('description')

    query = f"""
        INSERT INTO changes (description, changerid) VALUES
        (%s, %s);
    """
    data = (description, changerid)
    # executing and committing the insert statement
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()

    response = make_response("Successfully added change")
    response.status_code = 200
    return response

#------------------------------------------------------------
# Deletes a change in the changelog
@admins.route('/changelog/<changeid>', methods=['DELETE'])
def delete_change(changeid):

    query = f"""
        DELETE FROM changes WHERE id=%s;"""
    data = (changeid)
    # executing and committing the insert statement
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()

    response = make_response("Successfully added change")
    response.status_code = 200
    return response

#------------------------------------------------------------

@admins.route('/articles_per_month', methods=['GET'])
def get_articles_per_month():
    cursor = db.get_db().cursor()

    # Debugging the query execution
    query = '''
        SELECT
            YEAR(date) AS year,
            MONTH(date) AS month,
            COUNT(*) AS article_count
        FROM
            article
        GROUP BY
            YEAR(date), MONTH(date)
        ORDER BY
            YEAR(date), MONTH(date);
    '''

    logging.debug(f"Executing query: {query}")
    cursor.execute(query)

    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200

    logging.debug(f"Fetched rows: {theData}")

    cursor.execute('SELECT DATABASE();')
    db_name = cursor.fetchone()
    logging.debug(f"Connected to database: {db_name}")

    return response

#------------------------------------------------------------

@admins.route('/users_joined_per_week', methods=['GET'])
def get_users_joined_per_week():
    cursor = db.get_db().cursor()

    # Debugging the query execution
    query = '''
        SELECT
            YEAR(join_date) AS year,
            WEEK(join_date) AS week,
            COUNT(*) AS user_count
        FROM
            user
        GROUP BY
            YEAR(join_date), WEEK(join_date)
        ORDER BY
            YEAR(join_date), WEEK(join_date);
    '''

    logging.debug(f"Executing query: {query}")
    cursor.execute(query)

    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200

    logging.debug(f"Fetched rows: {theData}")

    cursor.execute('SELECT DATABASE();')
    db_name = cursor.fetchone()
    logging.debug(f"Connected to database: {db_name}")

    return response

#------------------------------------------------------------

@admins.route('/jobs_listed_per_week', methods=['GET'])
def get_jobs_listed_per_week():
    cursor = db.get_db().cursor()

    # Debugging the query execution
    query = '''
        SELECT
            YEAR(post_date) AS year,
            WEEK(post_date) AS week,
            COUNT(*) AS listing_count
        FROM
            jobListing
        GROUP BY
            YEAR(post_date), WEEK(post_date)
        ORDER BY
            YEAR(post_date), WEEK(post_date);
    '''

    logging.debug(f"Executing query: {query}")
    cursor.execute(query)

    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200

    logging.debug(f"Fetched rows: {theData}")

    cursor.execute('SELECT DATABASE();')
    db_name = cursor.fetchone()
    logging.debug(f"Connected to database: {db_name}")

    return response

#------------------------------------------------------------

@admins.route('/messages_sent_per_week', methods=['GET'])
def get_messages_sent_per_week():
    cursor = db.get_db().cursor()

    # Debugging the query execution
    query = '''
        SELECT
            YEAR(send_datetime) AS year,
            WEEK(send_datetime) AS week,
            COUNT(*) AS message_count
        FROM
            message
        GROUP BY
            YEAR(send_datetime), WEEK(send_datetime)
        ORDER BY
            YEAR(send_datetime), WEEK(send_datetime);
    '''

    logging.debug(f"Executing query: {query}")
    cursor.execute(query)

    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200

    logging.debug(f"Fetched rows: {theData}")

    cursor.execute('SELECT DATABASE();')
    db_name = cursor.fetchone()
    logging.debug(f"Connected to database: {db_name}")

    return response

#------------------------------------------------------------

@admins.route('/user_count_per_role', methods=['GET'])
def get_user_count_per_role():
    cursor = db.get_db().cursor()

    # Debugging the query execution
    query = '''
        SELECT role, COUNT(*) AS user_count
        FROM user
        GROUP BY role;
    '''

    logging.debug(f"Executing query: {query}")
    cursor.execute(query)

    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200

    logging.debug(f"Fetched rows: {theData}")

    cursor.execute('SELECT DATABASE();')
    db_name = cursor.fetchone()
    logging.debug(f"Connected to database: {db_name}")

    return response

from flask import jsonify, make_response
import logging

#------------------------------------------------------------

@admins.route('/applications_per_job_listing', methods=['GET'])
def get_applications_per_job_listing():
    cursor = db.get_db().cursor()

    query = '''
        SELECT
            jl.id AS job_listing_id,
            jl.title AS job_title,
            COUNT(a.id) AS application_count
        FROM
            jobListing jl
        LEFT JOIN
            application a ON jl.id = a.listingID
        GROUP BY
            jl.id, jl.title
        ORDER BY
            application_count DESC;
    '''


    cursor.execute(query)

    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


#------------------------------------------------------------

@admins.route('/average_gpa_per_job_listing', methods=['GET'])
def get_average_gpa_per_job_listing():
    cursor = db.get_db().cursor()

    query = '''
        SELECT
            jl.id AS job_listing_id,
            jl.title AS job_title,
            AVG(s.gpa) AS average_gpa
        FROM
            jobListing jl
        JOIN
            application a ON jl.id = a.listingID
        JOIN
            student s ON a.applicantID = s.id
        GROUP BY
            jl.id, jl.title
        ORDER BY
            average_gpa DESC;
    '''


    cursor.execute(query)

    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------

@admins.route('/most_common_majors', methods=['GET'])
def get_most_common_majors():
    cursor = db.get_db().cursor()

    query = '''
        SELECT
            s.major,
            COUNT(*) AS applicant_count
        FROM
            student s
        JOIN
            application a ON s.id = a.applicantID
        GROUP BY
            s.major
        ORDER BY
            applicant_count DESC;
    '''


    cursor.execute(query)

    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
#------------------------------------------------------------

@admins.route('/applications_per_week', methods=['GET'])
def get_applications_per_week():
    cursor = db.get_db().cursor()

    query = '''
        SELECT
            YEAR(submit_date) AS year,
            WEEK(submit_date) AS week,
            COUNT(*) AS application_count
        FROM
            application
        GROUP BY
            YEAR(submit_date), WEEK(submit_date)
        ORDER BY
            YEAR(submit_date), WEEK(submit_date);
    '''


    cursor.execute(query)

    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#----------------------------------------------------------------------------------------------------------
@admins.route('/average_query_execution_time', methods=['GET'])
def get_average_query_execution_time():
    try:
        cursor = db.get_db().cursor()

        query = '''
            SELECT
    EVENT_NAME, ROUND(SUM_TIMER_WAIT/COUNT_STAR/1000000000000, 6) AS avg_exec_time_ms
FROM
    performance_schema.events_statements_summary_global_by_event_name
WHERE
    COUNT_STAR > 0 AND EVENT_NAME LIKE 'statement/sql/%';
        '''

        cursor.execute(query)

        theData = cursor.fetchall()
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    except Exception as e:
        logging.error(f"Error in get_average_query_execution_time: {str(e)}")
        return make_response(jsonify({'error': 'Internal Server Error'}), 500)

#----------------------------------------------------------------------------------------------------------
@admins.route('/number_of_slow_queries', methods=['GET'])
def get_number_of_slow_queries():
    try:
        cursor = db.get_db().cursor()
        query = "SHOW GLOBAL STATUS LIKE 'Slow_queries';"

        cursor.execute(query)

        theData = cursor.fetchall()
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    except Exception as e:
        logging.error(f"Error in get_number_of_slow_queries: {str(e)}")
        return make_response(jsonify({'error': 'Internal Server Error'}), 500)

#----------------------------------------------------------------------------------------------------------

@admins.route('/number_of_connections', methods=['GET'])
def get_number_of_connections():
    try:
        cursor = db.get_db().cursor()
        query = "SHOW STATUS WHERE `variable_name` = 'Threads_connected';"

        cursor.execute(query)

        theData = cursor.fetchall()
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    except Exception as e:
        logging.error(f"Error in get_number_of_connections: {str(e)}")
        return make_response(jsonify({'error': 'Internal Server Error'}), 500)
#----------------------------------------------------------------------------------------------------------
@admins.route('/database_uptime', methods=['GET'])
def get_database_uptime():
    try:
        cursor = db.get_db().cursor()
        query = "SHOW GLOBAL STATUS LIKE 'Uptime';"

        cursor.execute(query)

        theData = cursor.fetchall()
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    except Exception as e:
        logging.error(f"Error in get_database_uptime: {str(e)}")
        return make_response(jsonify({'error': 'Internal Server Error'}), 500)
#----------------------------------------------------------------------------------------------------------

@admins.route('/table_sizes', methods=['GET'])
def get_table_sizes():
    try:
        cursor = db.get_db().cursor()
        query = '''
            SELECT
                table_name,
                ROUND((data_length + index_length) / 1024 / 1024, 2) AS size_mb
            FROM
                information_schema.TABLES
            WHERE
                table_schema = 'coffeeStats'
            ORDER BY
                size_mb DESC;
        '''

        cursor.execute(query)

        theData = cursor.fetchall()
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    except Exception as e:
        logging.error(f"Error in get_table_sizes: {str(e)}")
        return make_response(jsonify({'error': 'Internal Server Error'}), 500)

# ----------------------------------------------------------------------------------------------------------

@admins.route('/table_row_counts', methods=['GET'])
def get_table_row_counts():
    try:
        cursor = db.get_db().cursor()
        query = '''
            SELECT
                table_name,
                table_rows
            FROM
                information_schema.TABLES
            WHERE
                table_schema = 'coffeeStats';
        '''

        cursor.execute(query)

        theData = cursor.fetchall()
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    except Exception as e:
        logging.error(f"Error in get_table_row_counts: {str(e)}")
        return make_response(jsonify({'error': 'Internal Server Error'}), 500)


