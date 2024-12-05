##################################################
# Co-op Opportunities
##################################################

import streamlit as st
import requests

# Page title
st.title("Recommended Co-op Opportunities")
st.write("Browse co-op job listings relevant to your major.")

# Select the student's major
major = st.selectbox("Select your major:", ["Computer Science", "Business", "Engineering", "Biology", "Other"])

# Display relevant job listings based on selected major
st.write(f"### Co-op Opportunities for {major} Majors:")

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