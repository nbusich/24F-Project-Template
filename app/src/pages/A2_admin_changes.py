import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
import streamlit as st
import requests
import pandas as pd


st.set_page_config(layout = 'wide')

SideBarLinks()

# Dashboard title
st.header('Change Log')

response = requests.get('http://api:4000/admin/changelog').json()
df = pd.DataFrame(response)


# Create a container for the job listings
jobStuff = st.container(border = True)

with jobStuff:
    for i in range(-1, len(df)):
        row = st.container(border = True)

        with row:
            title, firstname, lastname, lastChange, desc = st.columns(5)

            # Display column headers for the first row
            if i == -1:
                with title:
                    st.button('**Category**')
                with firstname:
                    st.button('**First Name**')
                with lastname:
                    st.button('**Last Name**')
                with lastChange:
                    st.button('**Last Change**')
                with desc:
                    st.button('**Description**')
                continue

            # For other rows, display the content
            with title:
                st.button(label=df.iloc[i]['description'], type='primary', key=f"{i}_desc")
            with firstname:
                st.write(df.iloc[i]['firstname'])
            with lastname:
                st.write(df.iloc[i]['lastname'])
            with lastChange:
                st.write(df.iloc[i]['lastChange'][:16])
            with desc:
                st.write(df.iloc[i]['description'][:16] + '...')
