import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title('Find Pertinent Information')

# add a button to use the values entered into the number field to send to the 
# prediction function via the REST API
if st.button('View Current Application Statistics',
             type='primary',
             use_container_width=True):
  
  
  r = requests.get(f'http://api:4000/advisors/jobListingData').json()
  st.dataframe(r)

stu_id = st.number_input('Student Id:',
                           step=1)

logger.info(f'stu_id = {stu_id}')

# add a button to use the values entered into the number field to send to the 
# prediction function via the REST API
if st.button('Get Relevant Co-ops for Given Student',
             type='primary',
             use_container_width=True):
  results = requests.get(f'http://api:4000/advisors/studentRecs/{stu_id}').json()
  st.dataframe(results)
  