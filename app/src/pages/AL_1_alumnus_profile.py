# profile page for an alumnus 
# ----------------------------------------------------------
import logging
logger = logging.getLogger(__name__)
import requests

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

## ----------- functions ----------------------

def getItem(url, item_name):
    try:
        response = requests.get(url)
        response.raise_for_status()
        result = response.json()
        item = result[0][item_name] if result else item_name
    except requests.exceptions.RequestException as e:
        logger.error(f"Error getting item: {e} {item_name} {url}")
        item = "Error getting item"
    return item


def putItem(url, payload):
    try:
        response = requests.put(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error in putItem: {e}")

## -------------------------------------------------------------

## State initialization ----------------------------------------

alumnus_id = 289

if "data_fetched" not in st.session_state:
    st.session_state.curr_pos = getItem(f"http://api:4000/alumnus/alumnJobTitle/{alumnus_id}", "comment") or "N/A"
    st.session_state.curr_email = getItem(f"http://api:4000/alumnus/alumnusEmail/{alumnus_id}", "email") or "N/A"
    logger.info("email fetched!!!")

    st.session_state.curr_bio = "Add a bio"  
    st.session_state.edit = False
    st.session_state.data_fetched = True

job_title = st.session_state.curr_pos
job_id = getItem(f"http://api:4000/alumnus/positionByComment/{job_title}", 'id')
logger.info(f"Got job ID: {job_id}")

## -------------------------------------------------------------

# Page Title
st.title(f"Welcome, {st.session_state.get('first_name', 'Alumnus')}")

# Edit and Save Buttons
col_buttons = st.columns(2)
with col_buttons[0]:
    if st.button(label="✎"):
        st.session_state.edit = True

with col_buttons[1]:
    if st.button(label="Save"):
        if st.session_state.edit:
            st.session_state.edit = False
            putItem(f"http://api:4000/alumnus/update_job", {"id": alumnus_id, "job_id": job_id})
            logger.info(f"put email: {st.session_state.curr_email}")
            putItem(f"http://api:4000/alumnus/update_email", {"id": alumnus_id, "email": st.session_state.curr_email})
            logger.info(f"Saved email: {st.session_state.curr_email}")
            logger.info(f"Saved position: {st.session_state.curr_pos}")



col1, col2, col3 = st.columns(3)


with col1:
    st.markdown("### Current Position")
    if st.session_state.edit:
        st.text_input(
            "Add a job",
            value=st.session_state.curr_pos,
            key="curr_pos"
        )
    else:
        st.text(st.session_state.curr_pos)


with col2:
    st.markdown("### Bio")
    if st.session_state.edit:
        st.text_area(
            "Add a bio",
            value=st.session_state.curr_bio,
            key="curr_bio"
        )
    else:
        st.text(st.session_state.curr_bio)


with col3:
    st.markdown("### Email")
    logger.info(f"in col outside email is: {st.session_state.curr_email}")
   
    if st.session_state.edit:
        st.text_input("Add an email",
            value=st.session_state.curr_email,
            key="curr_email"
        )
        logger.info(f"in col email is: {st.session_state.curr_email}")
    else:
        st.text(st.session_state.curr_email)
