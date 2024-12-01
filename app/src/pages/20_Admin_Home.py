import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
import streamlit as st
import pandas as pd
import altair as alt
import requests
import time
from datetime import datetime


st.set_page_config(layout = 'wide')

SideBarLinks()

# Dashboard title
st.markdown("<div style='padding-top: -50px;font-size:18px; text-align:left; color:black;'>System Administrator Dashboard</div>", unsafe_allow_html=True)

data = {}

response = requests.get('http://api:4000/dashboard')
print(response.status_code)  # Print the HTTP status code
print(response.text)         # Print the raw response text

st.dataframe(response)

