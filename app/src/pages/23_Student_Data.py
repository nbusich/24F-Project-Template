##################################################
# Co-op Opportunities
##################################################

import requests
import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Sidebar links for the role of the currently logged-in user
SideBarLinks()

st.title("Student Data:")

# Fetch the current student ID from session state
student_id = st.session_state.get('studentID', None)

if not student_id:
    st.error("Student ID not found in session. Please log in again.")
    st.stop()

logger.info(f'Session mapped to Student ID: {student_id}')

# Fetch data from the updated route
def fetch_student_data(student_id):
    endpoint = f'http://api:4000/students/{student_id}'

    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.warning(f"Failed to fetch data from {endpoint}. Using dummy data.")
        logger.error(f"API Error: {e}")
        return None

# Fetch student data
student_data = fetch_student_data(student_id)

if not student_data:
    st.error("Could not fetch student data. Please try again later.")
    st.stop()

# Display student profile
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.write("**First Name:**", student_data.get("firstName", "N/A"))
    st.write("**Last Name:**", student_data.get("lastName", "N/A"))
    st.write("**Bio:**", student_data.get("bio", "N/A"))
    
with col2:
    st.write("**Major:**", student_data.get("major", "N/A"))
    st.write("*Minor:*", student_data.get())
    st.write("**Graduation Year:**", student_data.get("graduation_year", "N/A"))
    
st.divider()

# Additional functionality for updating stats or skills, if applicable
if st.button("Edit Profile"):
    with st.form("update_form"):
        updated_first_name = st.text_input("First Name", value=student_data.get("firstName", ""))
        updated_last_name = st.text_input("Last Name", value=student_data.get("lastName", ""))
        updated_major = st.text_input("Major", value=student_data.get("major", ""))
        updated_minor = st.text_input("Minor", value=student_data.get("minor", ""))
        updated_bio = st.text_area("Bio", value=student_data.get("bio", ""))
        updated_grad_year = st.number_input("Graduation Year", value=student_data.get("graduation_year", 2025), step=1)

        submit_update = st.form_submit_button("Submit")

        if submit_update:
            payload = {
                "firstName": updated_first_name,
                "lastName": updated_last_name,
                "bio": updated_bio,
                "major": updated_major,
                "minor": updated_minor,
                "graduation_year": updated_grad_year,
            }
            try:
                response = requests.put(f'http://api:4000/students/{student_id}', json=payload)
                response.raise_for_status()
                st.success("Profile updated successfully!")
            except Exception as e:
                st.error("Failed to update profile.")
                logger.error(f"Update Error: {e}")