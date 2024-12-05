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

st.title("Co-op Analysis: Compare Your Stats")

# Fetch the current student ID from session state
student_id = st.session_state.get('student_id', None)

if not student_id:
    st.error("Student ID not found in session. Please log in again.")
    st.stop()

logger.info(f'Session mapped to Student ID: {student_id}')

# Helper function to fetch data from the API
def fetch_data(endpoint, fallback):
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.warning(f"Failed to connect to {endpoint}. Using dummy data.")
        logger.error(f"API Error: {e}")
        return fallback

# Dummy data as a fallback
dummy_student_data = {
    "id": student_id,
    "name": "Vinny Test",
    "major": "Computer Science",
    "gpa": 3.7,
    "skills": ["Python", "SQL", "Machine Learning"],
    "relevantFields": ["Web Development", "Data Science"],
    "relevantMajors": ["Software Engineering", "Data Analytics"],
}

# Fetch student data
student_data = fetch_data(
    f'http://api:4000/student/profile/{student_id}',
    fallback=dummy_student_data
)

# Display student profile
st.subheader("Student Profile")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.write("**Major:**", student_data.get("major", "N/A"))
    st.write("**GPA:**", student_data.get("gpa", "N/A"))

with col2:
    st.write("**Skills:**", ", ".join(student_data.get("skills", [])))

# Display relevant majors and fields
show_majors, show_fields = st.columns(2)

with show_majors:
    st.pills(
        label="Relevant Majors:",
        options=student_data.get("relevantMajors", []),
        disabled=True,
        default=student_data.get("relevantMajors", []),
    )

with show_fields:
    st.pills(
        label="Relevant Fields:",
        options=student_data.get("relevantFields", []),
        disabled=True,
        default=student_data.get("relevantFields", []),
    )

st.divider()

# Update student stats
if st.button("Edit Stats"):
    with st.form("update_form"):
        updated_gpa = st.number_input("Update GPA", value=student_data.get("gpa", 0.0), step=0.1)
        updated_skills = st.text_area("Update Skills", value=", ".join(student_data.get("skills", [])))
        submit_update = st.form_submit_button("Submit")

        if submit_update:
            # Prepare payload for API update
            payload = {
                "gpa": updated_gpa,
                "skills": [skill.strip() for skill in updated_skills.split(",")],
            }
            try:
                response = requests.put(f'http://api:4000/student/profile/{student_id}', json=payload)
                response.raise_for_status()
                st.success("Profile updated successfully!")
            except Exception as e:
                st.error("Failed to update profile.")
                logger.error(f"Update Error: {e}")