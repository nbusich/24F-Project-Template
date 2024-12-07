import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests
from datetime import datetime

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()


######


listingID = st.session_state['current_listing']
#listingID = 32

logger.info(f'listingID = {listingID}')


data = {} 
try:
  data = requests.get(f'http://api:4000/comp/jobListing/{listingID}').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}



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

#the majors and fields for this job##
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
#####



num_applicants = data[0].get('numApplicants')
pay = data[0].get('payPerHour')
openings = data[0].get('numOpenings')
gpa = data[0].get('requiredGPA')
desc = data[0].get('description')
deadline = data[0].get('applicationDeadline')[5:16]

#Sun, 29 Dec 2024 00:00:00 GMT

deadline =  datetime.strptime(deadline, '%d %b %Y' )





companyid = st.session_state['compID']

st.title('Edit a Job Listing')

listing_title = st.text_input('Title', value=data[0].get('title'))

# create a 4 column layout
col1, col2, col3, col4 = st.columns(4)

# add one number input for number of applicants into column 1
with col1:
  number_of_applicants = st.number_input('\# Applicants', value=num_applicants,
                           step=1, min_value = 0)

# add another number input for pay into column 2
with col2:
  listing_pay = st.number_input('Pay per Hour ($)', value = pay,
                           step=0.01, min_value = 0.0)

# add another number input for number of openings into column 3
with col3:
  listing_openings = st.number_input('\# Openings', value = openings,
                           step=1, min_value = 0)
  
# add another number input for required GPA into column 4
with col4:
  listing_req_gpa = st.number_input('Required GPA', value=gpa, 
                           step=0.25, max_value=4.0, min_value = 0.0)
  
listing_description = st.text_area('Job Description', value=desc)

listing_deadline = st.date_input('Application Deadline', value=deadline)

rel_majors = st.multiselect(label='Relevant Majors', options=ex_majors, default=majors)

rel_fields = st.multiselect(label='Relevant Fields', options=ex_fields, default=fields)

new_majors = []
for i in range(0, len(rel_majors)):
  if rel_majors[i] not in majors:
    new_majors.append(rel_majors[i])

new_fields = []
for i in range(0, len(rel_fields)):
  if rel_fields[i] not in fields:
    new_fields.append(rel_fields[i])


dropped_majors = []
for i in range(0, len(majors)):
  if majors[i] not in rel_majors:
    dropped_majors.append(majors[i])

dropped_fields = []
for i in range(0, len(fields)):
  if fields[i] not in rel_fields:
    dropped_fields.append(fields[i])

logger.info(f'listing_title = {listing_title}')
logger.info(f'listing_description = {listing_description}')
logger.info(f'number_of_applicants = {number_of_applicants}')
logger.info(f'listing_pay = {listing_pay}')
logger.info(f'listing_deadline = {listing_deadline}')
logger.info(f'listing_openings = {listing_openings}')
logger.info(f'listing_req_gpa = {listing_req_gpa}')
logger.info(f'companyid = {companyid}')
logger.info(f'new_majors = {new_majors}')
logger.info(f'new_fields = {new_fields}')
logger.info(f'dropped_majors = {dropped_majors}')
logger.info(f'dropped_fields = {dropped_fields}')

if st.button('Update Job Listing',
             type='primary',
             use_container_width=True):
  
  update_data={'listing_title': listing_title, 
        'listing_description': listing_description, 
        'number_of_applicants': number_of_applicants, 
        'listing_pay': listing_pay, 
        'listing_deadline': listing_deadline.isoformat(), 
        'listing_openings': listing_openings, 
        'listing_req_gpa': listing_req_gpa,
        'new_majors' : new_majors,
        'new_fields' : new_fields,
        'dropped_majors' : dropped_majors,
        'dropped_fields' : dropped_fields}
  
  r = requests.put(f'http://api:4000/comp/jobListing/{listingID}', json=update_data)
  st.write(r)

if st.button('Delete Job Listing',
             type='secondary',
             use_container_width=True):
  r = requests.delete(f'http://api:4000/comp/jobListing/{listingID}').json()
  st.switch_page('pages/18_My_Listings.py')
  #st.toast(r['message'])

