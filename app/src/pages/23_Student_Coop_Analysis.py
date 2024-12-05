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

st.title("Co-op Analysis")

# Select user major
major = st.selectbox("Select your major:", ["Computer Science", "Business", "Engineering", "Biology", "Chemistry", "Education", "Finance", "Mathematics", "Physics"])

st.write(f"### Analyze Co-op Opportunities for {major} Majors:")

# HTTP GET request to fetch job listings based on major
try:
    response = requests.get(f'http://api:4000/advisors/jobListingData', params={'major': major})
    if response.status_code == 200:
        job_listings = response.json()
        if job_listings:
            for job in job_listings:
                st.write(f"- **{job['title']}** at {job['companyName']} ({job['payPerHour']}/hour)")
                st.write(f"  - Location: {job['location']}, Openings: {job['numOpenings']}")
                st.write(f"  - Required GPA: {job['requiredGPA']}, Application Deadline: {job['applicationDeadline']}")
                st.write(f"  - Description: {job['description']}")
                st.write("---")
        else:
            st.info("No opportunities found for this major.")
    else:
        st.error("Failed to fetch job opportunities. Please try again later.")
except Exception as e:
    st.error(f"An error occurred: {e}")