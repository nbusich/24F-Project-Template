import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

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
  listing_pay = st.number_input('Pay per Hour',
                           step=1, min_value = 0)

# add another number input for number of openings into column 3
with col3:
  listing_openings = st.number_input('\# Openings',
                           step=1, min_value = 0)
  
# add another number input for required GPA into column 4
with col4:
  listing_req_gpa = st.number_input('Required GPA',
                           step=0.25, max_value=4.0, value=2.0, min_value = 0.0)
  
listing_description = st.text_area('Job Description')

listing_deadline = st.date_input('Application Deadline')

logger.info(f'listing_title = {listing_title}')
logger.info(f'listing_description = {listing_description}')
logger.info(f'number_of_applicants = {number_of_applicants}')
logger.info(f'listing_pay = {listing_pay}')
logger.info(f'listing_deadline = {listing_deadline}')
logger.info(f'listing_openings = {listing_openings}')
logger.info(f'listing_req_gpa = {listing_req_gpa}')

# add a button to use the values entered into the number field to send to the 
# prediction function via the REST API
if st.button('Post Job Listing',
             type='primary',
             use_container_width=True):
  
  post_data={listing_title: listing_title, 
        listing_description: listing_description, 
        number_of_applicants: number_of_applicants, 
        listing_pay: listing_pay, 
        listing_deadline: listing_deadline, 
        listing_openings: listing_openings, 
        listing_req_gpa: listing_req_gpa}
  
  r = requests.post(f'http://api:4000/comp/joblisting/', data=post_data)
  st.write(r)