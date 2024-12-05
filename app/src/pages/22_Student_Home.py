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

if st.button('💼 Related Co-op Opportunities', type='primary', use_container_width=True):
    st.switch_page('pages/23_Coop_Opportunities.py')

if st.button('📅 Schedule an Advising Session', type='primary', use_container_width=True):
    st.switch_page('pages/24_Advisor_Scheduler.py')

if st.button('☕️ Connect with Alumni & Peers', type='primary', use_container_width=True):
    st.switch_page('pages/25_Connections.py')


 links = {
        "Northeastern Co-op Portal": "https://northeastern-csm.symplicity.com/students/?signin_tab=0",
        "Academic Calendar": "https://registrar.northeastern.edu/calendar",
        "Student Support Services": "https://studentlife.northeastern.edu/",
        "Career Development Resources": "https://careers.northeastern.edu/",
        "University Libraries": "https://library.northeastern.edu/",
        "Health and Counseling Services": "https://www.northeastern.edu/uhcs/",
        "Student Clubs and Organizations": "https://northeastern.presence.io/",
    }

    for label, url in links.items():
        st.markdown(f"- [{label}]({url})")

    st.write("\n")

if __name__ == "__main__":
    display_student_links()
st.write("\n")
st.markdown(
    """
    <hr style="border:1px solid #eaeaea">
    <small>"Need help? Contact the Co-op Office or access": "https://northeastern.edu/coop-faqs"</small>
    """,
    unsafe_allow_html=True,
)