import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

st.title('Edit Student Data')

with st.container():
    st.markdown("Update Student Info")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        student_id = st.number_input('Student Id', step=1, min_value=0)

    with col2:
        advisor_id = st.number_input('Advisor Id', step=1, min_value=0)

    with col3:
        resume = st.text_area('Student Resume')

    logger.info(f'student_id = {student_id}')
    logger.info(f'advisor_id = {advisor_id}')
    logger.info(f'resume = {resume}')

    if st.button('Update Student Info', type='primary', use_container_width=True):
        post_data = {'student_id': student_id, 'advisor_id': advisor_id, 'resume': resume}

        r = requests.put('http://api:4000/advisors/updateStudent', json=post_data)

        if r.status_code == 200:
            st.success(r.text)
        else:
            st.error(f"Error: {r.text} (Status code: {r.status_code})")
