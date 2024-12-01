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
try:
  data = requests.get('http://api:4000/p/dashboard').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)

