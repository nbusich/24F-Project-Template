import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

st.session_state['current_listing'] = 1

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome HR Contact, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Post a Job Listing', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/15_Create_Listing.py')

if st.button('View all Job Listings', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/17_All_Listings.py')


