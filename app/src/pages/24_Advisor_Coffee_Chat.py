##################################################
# Advisor Coffee Chat
##################################################

import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Sidebar links for the role of the currently logged-in user
SideBarLinks()
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