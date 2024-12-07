import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

st.session_state['current_listing'] = 1

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

compID = st.session_state['compID']

c = {} 
try:
  c = requests.get(f'http://api:4000/comp/myCompany/{compID}')
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  c = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}



st.session_state['compName'] = c.json()[0].get('name')

st.title(f"Welcome HR Contact, {st.session_state['first_name']}.")
st.markdown('##### Company: ' + st.session_state['compName'])
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Post a Job Listing', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/15_Create_Listing.py')

if st.button('My Job Listings', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/18_My_Listings.py')

st.divider()

if st.button('View All Job Listings', 
             type='secondary',
             use_container_width=True):
  st.switch_page('pages/17_All_Listings.py')

