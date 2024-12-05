##################################################
# Co-op Opportunities
##################################################

import streamlit as st
import requests

st.set_page_config(layout='wide')
st.title("Co-op Opportunities")

student_id = st.session_state.get('studentID', 1)  # Default to 1 for demo purposes

# API endpoint to fetch co-op jobs for the student's major
api_url = f"http://api:4000/students/{student_id}/coop_jobs"

# Fetch job listings from the backend API
response = requests.get(api_url)

if response.status_code == 200:
    job_listings = response.json()  # Parse JSON response

    # Display job listings or a message if none are available
    if len(job_listings) == 0:
        st.write("No co-op opportunities found for your major.")
    else:
        st.write("### Co-op Opportunities Related to Your Major:")
        for job in job_listings:
            st.subheader(job['title'])
            st.write(f"**Description:** {job['description']}")
            st.write(f"**Number of Openings:** {job['numOpenings']}")
            st.write(f"**Pay Per Hour:** ${job['payPerHour']}")
            st.write(f"**Company ID:** {job['companyID']}")
            st.write("---")
else:
    st.error("Unable to fetch co-op opportunities. Please try again later.")