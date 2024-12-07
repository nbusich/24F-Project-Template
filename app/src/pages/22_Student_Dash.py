##################################################
# Student Dashboard
##################################################

import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

# Welcome
st.title(f"Welcome, {st.session_state.get('first_name')}!")

st.write('### What would you like to do today?')

# Link to pages
if st.button('📃 Explore Co-op Listings', type='primary', use_container_width=True):
    st.switch_page('pages/pages/17_All_Listings.py')

if st.button('📎 Useful Student Links', type='primary', use_container_width=True):
    st.switch_page('pages/26_Student_Links_Chat.py')

st.write("\n")
st.markdown(
    """
    <hr style="border:1px solid #eaeaea">
    <div style="text-align: center;">
        <small>Need help? Contact the Co-op Office or visit our <a href="https://northeastern.edu/coop-faqs" target="_blank">FAQs</a>.</small>
    </div>
    """,
    unsafe_allow_html=True,
)
        