# profile page for an alumnus 
# ----------------------------------------------------------
import logging
logger = logging.getLogger(__name__)
import requests

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.session_state['edit'] = False


## ----------- functions ----------------------


def getItem(url, item_name):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        result = response.json()
        item = result[0][item_name]
    except requests.exceptions.RequestException as e:
        logger.error(f"something happened with fetching item: {e} {item_name} {url}")
        item = "Error fetching item"
    return item


def putItem(url, item_name, item_call):
    try:
        info = {item_name: item_call}
        response = requests.put(url, json=info)
        response.raise_for_status()

        st.success("putItem updated successfully!")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error in put_Item: {e}")
        st.error("Failed to putItem.")
             
## -------------------------------------------------------------

# session state for editable

# Set title
st.title(f"Welcome, {st.session_state['first_name']}")

if st.button(label="✎"):   
     st.session_state['edit'] = True

if st.button(label="Save"):
    st.session_state['edit'] = False


col1, col2, col3 = st.columns(3)

## saved variables ----------------------------------------------------------------

alumnus_id = 4

job_title = getItem(f"http://api:4000/alumnus/alumnJobTitle/{alumnus_id}", 'comment')

job_id = getItem((f"http://api:4000/alumnus/positionByComment/{job_title}"), 'id')

get_job_url = (f"http://api:4000/alumnus/alumnJobTitle/{job_id}") 

update_job_url = (f"http://api:4000/alumnus/update_job/{alumnus_id}") 

job_id_url = (f"http://api:4000/alumnus/positionByComment/{job_title}")


 ## --------------------------------------------------------------------

with col1:
        
    if not st.session_state['edit']:
        st.markdown("### Current Position")
        st.text(job_title)

    elif st.session_state['edit']:
        st.markdown("### Current Position")
        job_title = st.text_input("Add a job", value=job_title)
        job_id = getItem(job_id_url, 'id')
        putItem(update_job_url, "id", alumnus_id)
        curr_pos = getItem(get_job_url, 'comment')
        curr_pos = job_title 


        
    


with col2:
    if st.session_state['edit']:
        st.markdown("### Bio")
        curr_bio = st.text_input("add a bio")
    else:
        curr_bio = st.text_input("add a bio")
        st.markdown("### Bio")
        st.text(curr_bio)

with col3:
    if st.session_state['edit']:
        st.markdown("### Email")
        curr_email = st.text_input("add an email")
    else:
        curr_email = "nothing"
        st.markdown("### Email")
        st.text("add an email")
    
    
def getItem(url, item_name):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        result = response.json()
        item = result[0][item_name]
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching item: {e} {item_name}")
        item = "Error fetching item"
    return item


def putItem(url, item_name, item_call):
    try:
        info = {item_name: item_call}
        response = requests.put(api_url, json=info)
        response.raise_for_status()

        st.success("ptItem updated successfully!")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error in put_Item: {e}")
        st.error("Failed to putItem.")
             







