##################################################
# Student Home Page
##################################################

import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

# Welcome
st.title(f"Welcome, {st.session_state.get('first_name', 'Vinny')}!")

st.write('### What would you like to do today?')

# Link to pages
if st.button('📇 Student Data', type='primary', use_container_width=True):
    st.switch_page('pages/23_Student_Data.py')

if st.button('📅 Schedule an Advising Session', type='primary', use_container_width=True):
    st.switch_page('pages/24_Advisor_Coffee_Chat.py')

if st.button('☕️ Connect with Alumni & Peers', type='primary', use_container_width=True):
    st.switch_page('pages/25_Student_Connections.py')

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
        