import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

# Dashboard title
st.title("System Administrator Dashboard")

