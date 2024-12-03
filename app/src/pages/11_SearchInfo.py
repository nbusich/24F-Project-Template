import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title('Find Pertinent Information')

# Button 1: View Current Application Statistics
if st.button('View Current Application Statistics',
             type='primary',
             use_container_width=True):
    r = requests.get(f'http://api:4000/advisors/jobListingData').json()
    st.dataframe(r)

# Input: Student ID
stu_id = st.number_input('Student Id:',
                         step=1)
logger.info(f'stu_id = {stu_id}')

# Button 2: Get Relevant Co-ops for Given Student
if st.button('Get Relevant Co-ops for Given Student',
             type='primary',
             use_container_width=True, 
             key='coops_button'):
    results = requests.get(f'http://api:4000/advisors/studentRecs/{stu_id}').json()
    st.dataframe(results)

# Button 3: Find Students to Connect (Student ID-based)
if st.button('Find Students to Connect',
             type='primary',
             use_container_width=True,
             key='connect_students_button'):
    results2 = requests.get(f'http://api:4000/advisors/studentConnect/{stu_id}').json()
    logger.info(results2)
    st.dataframe(results2)

# Input: Company ID
company_id = st.number_input('Company Id:',
                              step=1)
logger.info(f'company_id = {company_id}')

# Button 4: Find students that have worked at a given company
if st.button('Find Students That Have Worked at Given Company',
             type='primary',
             use_container_width=True,
             key='connect_company_button'):
    results3 = requests.get(f'http://api:4000/advisors/studentAtCompany/{company_id}').json()
    logger.info(results3)
    st.dataframe(results3)

#input: Application ID
app_id = st.number_input('Application Id:',
                              step=1)
logger.info(f'app_id = {app_id}')

# Button 4: Find students info for application
if st.button('Find Student Information for Application',
             type='primary',
             use_container_width=True,
             key='application_data_button'):
    results4 = requests.get(f'http://api:4000/advisors/applicationInfo/{app_id}').json()
    logger.info(results4)
    st.dataframe(results4)