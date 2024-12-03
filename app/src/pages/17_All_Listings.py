import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title('All Job Listings')

jobs_data = {} 
try:
  jobs_data = requests.get('http://api:4000/comp/jobListing').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  jobs_data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

jobStuff = st.container(border=True)

with jobStuff:
  for i in range(-1, len(jobs_data)):
    row = st.container(border=True)
    with row:
      
      title, comp, pay, deadline, desc = st.columns(5)

      if i == -1:
        with title:
          st.button('**Job Title**')
        with comp:
          st.button('**Company**')
        with pay:
          st.button('**Pay per Hour**')
        with deadline:
          st.button('**Deadline**')
        with desc:
          st.button('**Description**')
        continue

      with title:
        if st.button(label=jobs_data[i].get('title'), type='primary', help='View Full Listing', key=str(i) + 'title'):
          st.session_state['current_listing'] = i + 1
          st.write(jobs_data[i].get('jobListingID'))
          st.switch_page('pages/16_View_Listing.py')
      with comp:
        st.button(jobs_data[i].get('companyName'), key=str(i) + 'comp')
      with pay:
        st.write('$' + str(jobs_data[i].get('payPerHour')))
      with deadline:
        st.write(jobs_data[i].get('applicationDeadline')[:16])
      with desc:
        st.write(jobs_data[i].get('description')[:16] + '...')
