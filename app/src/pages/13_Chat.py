import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

st.title('Make or Delete Chats')

# Add or delete a chat
with st.container():
    st.markdown('Start or Delete a Chat')

    # Advisor ID is fetched from session state (assumes it's already set)
    if 'adv_id' not in st.session_state:
        st.error("Advisor ID not found in session state. Please log in or provide credentials.")
    else:
        adv_id = st.session_state['adv_id']

        # Input for company ID
        comp_id = st.number_input('Company Id', step=1, min_value=0)

        # Create chat button
        if st.button('Make Chat', type='primary'):
            # Make POST request
            r = requests.post(f'http://api:4000/advisors/createcompanychat/{adv_id}/{comp_id}')

            if r.status_code == 200:
                st.success(r.text)
            else:
                st.error(f"Failed to create chat: {r.text}")

        if st.button('Delete Chat', type='primary'):
            response = requests.delete(f'http://api:4000/advisors/deletechat/{adv_id}/{comp_id}')

            if response.status_code == 200:
                st.success(response.text)
            else:
                st.error(f"Failed to delete chat: {response.text}")