##################################################
# Co-op Opportunities
##################################################

import requests
import streamlit as st
from modules.nav import SideBarLinks

SideBarLinks()

st.set_page_config(layout='wide')

st.title("Student Profile Overview")

# Fetch the current student ID from session state
student_id = st.session_state.get('studentID', None)

if not student_id:
    st.error("Student ID not found in session. Please log in again.")
    st.stop()

api_url = f"http://localhost:4000/students/{student_id}"

try:
    response = requests.get(api_url)
    response.raise_for_status()

    student_data = response.json()

    st.write(f"**Name:** {student_data.get('firstName', 'N/A')} {student_data.get('lastName', 'N/A')}")
    st.write(f"**Email:** {student_data.get('email', 'N/A')}")
    st.write(f"**Bio:** {student_data.get('bio', 'N/A')}")
    st.write(f"**Major:** {student_data.get('major', 'N/A')}")
    st.write(f"**Minor:** {student_data.get('minor', 'N/A')}")

except requests.exceptions.RequestException as e:
    st.error("Could not fetch student data. Please try again later.")
    st.error(f"Error: {e}")

