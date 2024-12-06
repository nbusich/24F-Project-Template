##################################################
# Co-op Opportunities
##################################################

import requests
import logging
import streamlit as st
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)

st.set_page_config(layout='wide')

SideBarLinks()

st.title("Student Profile")

# Fetch the current student ID from session state
student_id = st.session_state.get('studentID', None)
if not student_id:
    st.error("Student ID not found in session. Please log in again.")
    st.stop()

# Fetch data from the updated route
def fetch_student_data(url, key):
    try:
        response = requests.get(url)
        response.raise_for_status()
        result = response.json()
        return result.get(key, f"{key} not found")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching {key}: {e}")
        return f"Error fetching {key}"

def update_student_data(url, payload):
    try:
        response = requests.put(url, json=payload)
        response.raise_for_status()
        st.success("Data updated successfully!")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error updating data: {e}")
        st.error("Failed to update data.")

base_url = "http://api:4000/students"
profile_url = f"{base_url}/{student_id}"
update_url = f"{base_url}/{student_id}"

st.divider()

try:
    response = requests.get(profile_url)
    response.raise_for_status()
    student_data = response.json()
except requests.exceptions.RequestException as e:
    st.error("Could not fetch student data. Please try again later.")
    logger.error(f"API Error: {e}")
    st.stop()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Name")
    if st.session_state["edit"]:
        name = st.text_input("Edit Name", value=f"{student_data.get('firstName', '')} {student_data.get('lastName', '')}")
    else:
        st.text(f"{student_data.get('firstName', 'N/A')} {student_data.get('lastName', 'N/A')}")

with col2:
    st.markdown("### Email")
    if st.session_state["edit"]:
        email = st.text_input("Edit Email", value=student_data.get("email", ""))
    else:
        st.text(student_data.get("email", "N/A"))

with col3:
    st.markdown("### Bio")
    if st.session_state["edit"]:
        bio = st.text_area("Edit Bio", value=student_data.get("bio", ""))
    else:
        st.text(student_data.get("bio", "N/A"))

st.divider()

col4, col5 = st.columns(2)

with col4:
    st.markdown("### Major")
    if st.session_state["edit"]:
        major = st.text_input("Edit Major", value=student_data.get("major", ""))
    else:
        st.text(student_data.get("major", "N/A"))

with col5:
    st.markdown("### Minor")
    if st.session_state["edit"]:
        minor = st.text_input("Edit Minor", value=student_data.get("minor", ""))
    else:
        st.text(student_data.get("minor", "N/A"))

st.divider()

# Additional functionality for updating stats or skills, if applicable
if st.button("Edit Profile"):
    with st.form("update_form"):
        payload = {
            "firstName": name.split()[0],
            "lastName": name.split()[1] if len(name.split()) > 1 else "",
            "email": email,
            "bio": bio,
            "major": major,
            "minor": minor,
        }
        update_student_data(update_url, payload)