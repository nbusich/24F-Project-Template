import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

listingID = st.session_state['current_listing']

logger.info(f'jobNum = {listingID}')


data = {} 
try:
  data = requests.get(f'http://api:4000/comp/jobListing/{listingID}').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

majors_data = {} 
try:
  majors_data = requests.get(f'http://api:4000/comp/relevantMajors/{listingID}').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  majors_data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}


majors = []
for i in range(0, len(majors_data)):
  majors.append(majors_data[i].get('major'))

fields_data = {} 
try:
  fields_data = requests.get(f'http://api:4000/comp/relevantFields/{listingID}').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  fields_data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

fields = []
for i in range(0, len(fields_data)):
  fields.append(fields_data[i].get('field'))



listing_title = data[0].get('title')
st.title(listing_title)

listing_company = data[0].get('companyName')
st.markdown('#### ' + listing_company)

st.divider()

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
  number_of_applicants = st.number_input(label='\# Applicants', value=num_applicants, min_value=num_applicants, max_value=num_applicants)

# pay into column 2
with col2:
  listing_pay = st.number_input('Pay per Hour ($)', value=pay, min_value=pay, max_value=pay)

# number of openings into column 3
with col3:
  listing_openings = st.number_input('\# Openings', value=openings, min_value=openings, max_value=openings)
  
# required GPA into column 4
with col4:
  listing_req_gpa = st.number_input('Required GPA', value=gpa, min_value=gpa, max_value=gpa)
  
listing_description = st.container(border=True)
with listing_description:
  st.markdown(body=desc)

show_majors, show_fields = st.columns(2)

with show_majors:
  st.pills(label='Relevant Majors:', options=majors, disabled=False, default=majors, selection_mode='multi')

with show_fields:
  st.pills(label='Relevant Fields:', options=fields, disabled=False, default=fields, selection_mode='multi')

st.divider()

listing_deadline = st.write('Application Deadline:', deadline[:16])
