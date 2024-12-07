##################################################
# Co-op Opportunities
##################################################

import requests
import streamlit as st
from modules.nav import SideBarLinks

SideBarLinks()

st.set_page_config(layout='wide')

st.title("Student Profile Overview")

# Fetch the current student ID from session state
student_id = st.session_state.get('studentID')


