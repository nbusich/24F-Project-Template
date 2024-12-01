import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

data = {} 
try:
  data = requests.get('http://api:4000/comp/jobListing/1').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}


#st.dataframe(data)

listing_title = data[0].get('title')
st.title(listing_title)

listing_company = data[0].get('company.name')
st.header(listing_company)

num_applicants = data[0].get('numApplicants')
pay = data[0].get('payPerHour')
openings = data[0].get('numOpenings')
gpa = data[0].get('requiredGPA')
desc = data[0].get('description')
deadline = data[0].get('applicationDeadline')

# create a 4 column layout
col1, col2, col3, col4 = st.columns(4)

# number of applicants into column 1
with col1:
  number_of_applicants = st.text(num_applicants)

# pay into column 2
with col2:
  listing_pay = st.text(pay)

# number of openings into column 3
with col3:
  listing_openings = st.text(openings)
  
# required GPA into column 4
with col4:
  listing_req_gpa = st.text(gpa)
  
listing_description = st.markdown(body=desc)

listing_deadline = st.write(deadline)

