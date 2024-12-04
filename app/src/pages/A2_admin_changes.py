import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout = 'wide')
SideBarLinks()

tab1, tab2 = st.tabs(['View Changes', 'Make Changes'])
with tab1:

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
                    if st.button('Delete' + ' change'+ f' {i}'):
                        pass
with tab2:
    st.header('Make Changes')
    with st.container(border = True):
        st.markdown('Document a Change')
        changerID = st.session_state['adminID']
        description = st.text_area('Change Description')

        if st.button('Log Change',
                     type='primary'):
            post_data = {
                         'description': description, 'changerID': changerID
                         }

            r = requests.post(f'http://api:4000/admin/make_change', json=post_data)

            if r.status_code == 200:
                st.success(r.text)
            else:
                pass
    with st.container(border=True):
        # Streamlit UI
        st.markdown("Delete User")
        userid = st.text_input("User ID", "")
        username = st.text_input("Username", "")

        if st.button("Delete User", type = "primary"):
            if userid and username:
                # Call Flask API
                url = f"http://api:4000/admin/delete_user/{userid}/{username}"
                response = requests.delete(url)

                if response.status_code == 200:
                    st.success(response.text)
                else:
                    st.error(response.text)
            else:
                st.warning("Please enter both User ID and Username")

    with st.container(border = True):
        st.markdown("Update Job Listing")
        listing_title = st.text_input('Title')

        # create a 4 column layout
        col1, col2, col3, col4 = st.columns(4)

        # add one number input for number of applicants into column 1
        with col1:
            number_of_applicants = st.number_input('\# Applicants',
                                                   step=1, min_value=0)

        # add another number input for pay into column 2
        with col2:
            listing_pay = st.number_input('Pay per Hour ($)',
                                          step=1, min_value=0)

        # add another number input for number of openings into column 3
        with col3:
            listing_openings = st.number_input('\# Openings',
                                               step=1, min_value=0)

        # add another number input for required GPA into column 4
        with col4:
            listing_req_gpa = st.number_input('Required GPA',
                                              step=0.25, max_value=4.0, value=3.0, min_value=0.0)

        listing_description = st.text_area('Job Description')

        companyid = st.number_input('Company ID',
                                      step=1, min_value=0)

        id = st.number_input('Listing to update ID',
                                    step=1, min_value=0)

        listing_deadline = st.date_input('Application Deadline')

        logger.info(f'listing_title = {listing_title}')
        logger.info(f'listing_description = {listing_description}')
        logger.info(f'number_of_applicants = {number_of_applicants}')
        logger.info(f'listing_pay = {listing_pay}')
        logger.info(f'listing_deadline = {listing_deadline}')
        logger.info(f'listing_openings = {listing_openings}')
        logger.info(f'listing_req_gpa = {listing_req_gpa}')
        logger.info(f'companyid = {companyid}')
        logger.info(f'id = {id}')


        if st.button('Update Job Listing',
                     type='primary',
                     use_container_width=True):
            post_data = {'listing_title': listing_title,
                         'listing_description': listing_description,
                         'number_of_applicants': number_of_applicants,
                         'listing_pay': listing_pay,
                         'listing_deadline': listing_deadline.isoformat(),
                         'listing_openings': listing_openings,
                         'listing_req_gpa': listing_req_gpa,
                         'companyid': companyid,
                         'id': id}

            r = requests.put(f'http://api:4000/admin/update_app', json=post_data)
            st.write(r)



