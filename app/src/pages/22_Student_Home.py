##################################################
# Student Home Page
##################################################

import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Sidebar links for the role of the currently logged-in user
SideBarLinks()

# Welcome
st.title(f"Welcome, {st.session_state.get('first_name', 'Vinny')}!")

# Link to pages
st.write('### What would you like to do today?')

if st.button('🔍 Co-op Opportunities', type='primary', use_container_width=True):
    st.switch_page('pages/23_Coop_Opportunities.py')

if st.button('📅 Schedule an Advising Session', type='primary', use_container_width=True):
    st.switch_page('pages/24_Advisor_Scheduler.py')

if st.button('🤝 Connect with Alumni & Peers', type='primary', use_container_width=True):
    st.switch_page('pages/25_Connections.py')

# Additional features section
st.write("\n")
st.write("### Quick Links")
st.write("""
- [Northeastern Co-op Portal](https://northeastern-csm.symplicity.com/students/?signin_tab=0)
- [Academic Calendar](https://registrar.northeastern.edu/calendar)
- [Student Support Services](https://studentlife.northeastern.edu/)
""")

st.write("\n")
st.markdown(
    """
    <hr style="border:1px solid #eaeaea">
    <small>Need help? Contact the Co-op Office or access [FAQs](https://northeastern.edu/coop-faqs).</small>
    """,
    unsafe_allow_html=True,
)