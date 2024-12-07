##################################################
# Co-op Opportunities
##################################################

import requests
import streamlit as st
from modules.nav import SideBarLinks

SideBarLinks()

st.title("Student Profile")

# Fetch the current student ID from session state
id = st.session_state.get('studentID')

if not id:
    st.error("Student ID not found in session. Please log in again.")
    st.stop()

student_data_url = f"http://api:4000/students/studentList/id"

try:
    response = requests.get(student_data_url)
    response.raise_for_status()

    data = response.json()

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**ID:** {data.get('id')}")
        st.write(f"**Name:** {data.get('firstName')} {data.get('lastName')}")
        st.write(f"**Bio:** {data.get('bio')}")

    # Display student data in the second column
    with col2:
        st.write(f"**Major:** {data.get('major')}")
        st.write(f"**Minor:** {data.get('minor')}")
        st.write(f"**GPA:** {data.get('gpa')}")
        st.write(f"**Resume:** {data.get('resume')}")

except requests.exceptions.RequestException as e:
    st.error("Could not fetch student data. Please try again later.")
    st.error(f"Error: {e}")
