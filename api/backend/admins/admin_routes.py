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
    cursor.execute('''
                    SHOW STATUS
    WHERE Variable_name IN ('Com_admin_commands',
                        'Com_create_table',
                        'Com_delete',
                        'Com_insert',
                        'Com_select',
                        'Com_update',
                        'Innodb_rows_inserted',
                        'Innodb_rows_deleted',
                        'Mysqlx_connections_rejected',
                        'Mysqlx_errors_sent',
                        'Mysqlx_cursor_fetch',
                        'Queries',
                        'Uptime'
    );''')
    
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