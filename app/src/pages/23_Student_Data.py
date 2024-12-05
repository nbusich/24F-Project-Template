##################################################
# Co-op Opportunities
##################################################

import requests
import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

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
    fallback = {
        "id": student_id,
        "name": "Vinny Test",
        "email": "vinny.test@example.com",
        "major": "Computer Science",
        "graduation_year": 2025,
    }
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.warning(f"Failed to fetch data from {endpoint}. Using dummy data.")
        logger.error(f"API Error: {e}")
        return fallback

# Fetch student data
student_data = fetch_student_data(student_id)

# Display student profile
st.subheader(f"Email: {student_data['email']}")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.write("**Major:**", student_data.get("major", "N/A"))

with col2:
    st.write("**Graduation Year:**", student_data.get("graduation_year", "N/A"))

st.divider()

# Additional functionality for updating stats or skills, if applicable
if st.button("Edit Profile"):
    with st.form("update_form"):
        updated_major = st.text_input("Major", value=student_data.get("major", ""))
        updated_year = st.number_input("Graduation Year", value=student_data.get("graduation_year", 2025), step=1)
        submit_update = st.form_submit_button("Submit")

        if submit_update:
            # Prepare payload for update
            payload = {
                "major": updated_major,
                "graduation_year": updated_year,
            }
            try:
                response = requests.put(f'http://api:4000/students/{student_id}', json=payload)
                response.raise_for_status()
                st.success("Profile updated successfully!")
            except Exception as e:
                st.error("Failed to update profile.")
                logger.error(f"Update Error: {e}")