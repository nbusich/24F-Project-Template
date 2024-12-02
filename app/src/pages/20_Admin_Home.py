import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
import streamlit as st
import requests



st.set_page_config(layout = 'wide')

SideBarLinks()

# Dashboard title
st.markdown("<div style='padding-top: -50px;font-size:18px; text-align:left; color:black;'>System Administrator Dashboard</div>", unsafe_allow_html=True)

data = {}

response = requests.get('http://api:4000/admin/changelog').json()

st.dataframe(response)

