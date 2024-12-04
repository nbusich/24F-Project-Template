# profile page for an alumnus 
# ----------------------------------------------------------
import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.session_state['edit'] = False

# session state for editable

# Set title
st.title(f"Welcome, {st.session_state['first_name']}")

if st.button(label="✎"):   
     st.session_state['edit'] = True

if st.button(label="Save"):
    st.session_state['edit'] = False


col1, col2, col3 = st.columns(3)


with col1:
    curr_pos = st.text()
    if not st.session_state['edit']:
        st.markdown("### Current Position")
        st.text(curr_pos)
    if st.session_state['edit']:
        st.markdown("### Current Position")
        curr_pos = st.text_input("add a job")
    

with col2:
    curr_bio = st.text()
    if not st.session_state['edit']:
        st.markdown("### Bio")
        st.text(curr_bio)
    if st.session_state['edit']:
        st.markdown("### Bio")
        curr_bio = st.text_input("add a bio")

with col3:
    curr_bio = st.text()
    if not st.session_state['edit']:
         st.markdown("### Email")
         st.text("add an email")
    if st.session_state['edit']:
        st.markdown("### Location")
        curr_bio = st.text_input("add a location")
    
    st.markdown("### Location")
   











