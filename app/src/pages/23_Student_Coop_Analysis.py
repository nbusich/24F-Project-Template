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

# Get the student's ID dynamically
email_input = st.text_input("Enter your email to log in:", placeholder="example@domain.com")

if email_input:
    student_id = None
    student_data = {}
    try:
        # Fetch all students and find the user by email
        response = requests.get("http://api:4000/students")
        response.raise_for_status()
        all_students = response.json()
        
        # Search for the matching student by email
        for student in all_students:
            if student["email"] == email_input:
                student_id = student["id"]
                student_data = student
                break
        
        if not student_id:
            st.error("No student found with that email.")
    except Exception as e:
        st.error("Unable to fetch student data. Check API connection.")
        logger.error(e)

    if student_id:
        # Fetch co-op job listings relevant to the student
        coop_listings = []
        try:
            response = requests.get(f"http://api:4000/students/{student_id}/coop_jobs")
            response.raise_for_status()
            coop_listings = response.json()
        except Exception as e:
            st.error("Unable to fetch co-op job listings. Check API connection.")
            logger.error(e)

        # Display Student's Details
        if student_data:
            st.header(f"Welcome, {student_data['name']}!")
            st.subheader("Your Details")
            st.write(f"**Major:** {student_data['major']}")
            st.write(f"**Graduation Year:** {student_data['graduation_year']}")

        st.divider()

        # Display Relevant Co-op Listings
        st.subheader("Relevant Co-op Listings")

        if coop_listings:
            for job in coop_listings:
                st.markdown(f"### {job['title']} at Company ID: {job['companyID']}")
                st.write(f"**Description:** {job['description']}")
                st.write(f"**Pay per Hour:** ${job['payPerHour']}")
                st.write(f"**Openings:** {job['numOpenings']}")
                st.divider()
        else:
            st.warning("No co-op listings available for your major.")