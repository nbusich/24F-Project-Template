import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

companyid = st.session_state['compID']

st.title('Create a Job Listing')

listing_title = st.text_input('Title')

# create a 4 column layout
col1, col2, col3, col4 = st.columns(4)

# add one number input for number of applicants into column 1
with col1:
  number_of_applicants = st.number_input('\# Applicants',
                           step=1, min_value = 0)

# add another number input for pay into column 2
with col2:
  listing_pay = st.number_input('Pay per Hour ($)',
                           step=1, min_value = 0)

# add another number input for number of openings into column 3
with col3:
  listing_openings = st.number_input('\# Openings',
                           step=1, min_value = 0)
  
# add another number input for required GPA into column 4
with col4:
  listing_req_gpa = st.number_input('Required GPA',
                           step=0.25, max_value=4.0, value=3.0, min_value = 0.0)
  
listing_description = st.text_area('Job Description')

listing_deadline = st.date_input('Application Deadline')


#Major and Field lists###
all_majors = {} 
try:
  all_majors = requests.get(f'http://api:4000/comp/relevantMajors').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  all_majors = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

ex_majors = ['Computer Science', 'Biology', 'Data Science', 'Neuroscience', 'Mechanical Engineering', 'Civil Engineering', 'Music', 'Music Technology', 'Pre-med', 'English', 'Communications', 'Business', 'Economics', 'Theater', 'Art', 'Design', 'Finance']

for i in range(0, len(all_majors)):
  if all_majors[i].get('major') not in ex_majors:
    ex_majors.append(all_majors[i].get('major'))

all_fields = {} 
try:
  all_fields = requests.get(f'http://api:4000/comp/relevantFields').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  all_fields = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

ex_fields = ['Software Engineering', 'Information Technology', 'Biology', 'Data Analysis', 'Neuroscience', 'Mechanical Engineering', 'Civil Engineering', 'Music', 'Audio Engineering', 'Medical Research', 'Writing', 'Communications', 'Business', 'Economics', 'Theater', 'Art', 'Graphic Design']

for i in range(0, len(all_fields)):
  if all_fields[i].get('field') not in ex_fields:
    ex_fields.append(all_fields[i].get('field'))
####


rel_majors = st.multiselect(label='Relevant Majors', options=ex_majors)

rel_fields = st.multiselect(label='Relevant Fields', options=ex_fields)

logger.info(f'listing_title = {listing_title}')
logger.info(f'listing_description = {listing_description}')
logger.info(f'number_of_applicants = {number_of_applicants}')
logger.info(f'listing_pay = {listing_pay}')
logger.info(f'listing_deadline = {listing_deadline}')
logger.info(f'listing_openings = {listing_openings}')
logger.info(f'listing_req_gpa = {listing_req_gpa}')
logger.info(f'companyid = {companyid}')
logger.info(f'rel_majors = {rel_majors}')
logger.info(f'rel_fields = {rel_fields}')

if st.button('Post Job Listing',
             type='primary',
             use_container_width=True):
  
  post_data={'listing_title': listing_title, 
        'listing_description': listing_description, 
        'number_of_applicants': number_of_applicants, 
        'listing_pay': listing_pay, 
        'listing_deadline': listing_deadline.isoformat(), 
        'listing_openings': listing_openings, 
        'listing_req_gpa': listing_req_gpa,
        'companyid': companyid,
        'rel_majors' : rel_majors,
        'rel_fields' : rel_fields}
  
  r = requests.post(f'http://api:4000/comp/jobListing', json=post_data)
  st.write(r)
  st.switch_page('pages/18_My_Listings.py')

