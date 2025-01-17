import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

companyID = st.session_state['compID']
#companyID =4

st.title('My Job Listings')

jobs_data = {} 
try:
  jobs_data = requests.get(f'http://api:4000/comp/myJobListing/{str(companyID)}').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  jobs_data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

#st.dataframe(jobs_data)

jobStuff = st.container(border=True)

with jobStuff:
  for i in range(-1, len(jobs_data)):
    row = st.container(border=True)
    with row:
      
      title, pay, deadline, desc = st.columns([3, 2, 2, 2])

      if i == -1:
        with title:
          st.button('**Job Title** | click to edit')
        with pay:
          st.button('**Pay per Hour**')
        with deadline:
          st.button('**Deadline**')
        with desc:
          st.button('**Description**')
        continue

      with title:
        if st.button(label=jobs_data[i].get('title'), type='primary', help='Edit Listing', key=str(i) + 'title'):
          st.session_state['current_listing'] = (jobs_data[i].get('listingID'))
          st.switch_page('pages/19_Edit_Listing.py')
     
      with pay:
        st.write('$' + str(jobs_data[i].get('payPerHour')))
      with deadline:
        st.write(jobs_data[i].get('applicationDeadline')[4:16])
      with desc:
        st.write(jobs_data[i].get('description')[:16] + '...')