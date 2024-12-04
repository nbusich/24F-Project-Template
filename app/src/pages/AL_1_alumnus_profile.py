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
     st.session_state['edit'] = not st.session_state['edit']

col1, col2, col3 = st.columns(3)


with col1:
        st.markdown("### Current Position")
        curr_pos = st.text_area("add a job")


with col2:
    st.markdown("### Bio")
    st.text_area("add a bio")

with col3:
    st.markdown("### Location")
    st.text_area("add a location")











