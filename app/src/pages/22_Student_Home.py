##################################################
# Student Home Page
##################################################

import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Display appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

# Welcome
st.title(f"Welcome, {st.session_state.get('first_name', 'Vinny')}!")
st.subheader("Your personalized dashboard for co-op success at Northeastern.")
st.write("\n")

# Main Content
st.write('### What would you like to do today?')
st.write("Select one of the options below to get started:")

# Action Buttons for Key Features
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('🔍 Explore Co-op Opportunities', type='primary', use_container_width=True):
        st.switch_page('pages/23_Coop_Opportunities.py')

if st.button('📅 Schedule an Advising Session', type='primary', use_container_width=True):
    st.switch_page('pages/24_Advisor_Scheduler.py')

if st.button('🤝 Connect with Alumni & Peers', type='primary', use_container_width=True):
    st.switch_page('pages/25_Connections.py')

# Additional Features Section
st.write("\n")
st.write("### Quick Links")
st.write("""
- [Northeastern Co-op Portal](https://www.northeastern.edu/coop)
- [Academic Calendar](https://registrar.northeastern.edu/calendar)
- [Student Support Services](https://studentlife.northeastern.edu/)
""")

# Footer
st.write("\n")
st.markdown(
    """
    <hr style="border:1px solid #eaeaea">
    <small>Need help? Contact the Co-op Office or access [FAQs](https://northeastern.edu/coop-faqs).</small>
    """,
    unsafe_allow_html=True,
)