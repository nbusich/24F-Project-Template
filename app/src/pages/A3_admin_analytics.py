import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks
import plotly.express as px

SideBarLinks()

# Base URL for your API
BASE_URL = 'http://api:4000/admin'

# Function to fetch data from API endpoints
def fetch_data(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list):
            df = pd.DataFrame(data)
            if not df.empty:
                return df
            else:
                return None
        elif isinstance(data, dict):
            return data  # For endpoints returning a single value
        else:
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data from {endpoint}: {e}")
        return None

# Set the page title
st.header('Analytics Dashboard')

# Fetch data for existing metrics
articles_df = fetch_data('articles_per_month')
users_df = fetch_data('users_joined_per_week')
jobs_df = fetch_data('jobs_listed_per_week')
messages_df = fetch_data('messages_sent_per_week')
roles_df = fetch_data('user_count_per_role')

# Fetch data for new metrics
applications_per_job_listing_df = fetch_data('applications_per_job_listing')
average_gpa_per_job_listing_df = fetch_data('average_gpa_per_job_listing')
most_common_majors_df = fetch_data('most_common_majors')
applications_per_week_df = fetch_data('applications_per_week')

# First row of new charts
col1, col2 = st.columns(2)

with col1:
    st.markdown('Top Applications Per Job Listing')
    if applications_per_job_listing_df is not None:
        if not applications_per_job_listing_df.empty:
            top_n = 10
            top_applications_df = applications_per_job_listing_df.head(top_n)
            chart = px.bar(
                top_applications_df,
                x='job_title',
                y='application_count'
            )
            st.plotly_chart(chart)
        else:
            st.write("No data available for applications per job listing.")
    else:
        st.write("No data available for applications per job listing.")

with col2:
    st.markdown('Highest Average GPA of Applicants Per Job Listing')
    if average_gpa_per_job_listing_df is not None:
        if not average_gpa_per_job_listing_df.empty:
            top_n = 10
            top_gpa_df = average_gpa_per_job_listing_df.head(top_n)
            chart = px.bar(
                top_gpa_df,
                x='job_title',
                y='average_gpa'
            )
            st.plotly_chart(chart)
        else:
            st.write("No data available for average GPA per job listing.")
    else:
        st.write("No data available for average GPA per job listing.")

# Second row of new charts
col3, col4 = st.columns(2)

with col3:
    st.markdown('Most Common Majors Among Applicants')
    if most_common_majors_df is not None:
        if not most_common_majors_df.empty:
            chart = px.bar(
                most_common_majors_df,
                x='major',
                y='applicant_count'
            )
            st.plotly_chart(chart)
        else:
            st.write("No data available for applicants' majors.")
    else:
        st.write("No data available for applicants' majors.")

with col4:
    st.markdown('Applications Submitted Per Week')
    if applications_per_week_df is not None:
        if not applications_per_week_df.empty:
            applications_per_week_df['year_week'] = applications_per_week_df['year'].astype(str) + '-W' + applications_per_week_df['week'].astype(str)
            applications_chart = applications_per_week_df.set_index('year_week')['application_count']
            st.line_chart(applications_chart)
        else:
            st.write("No data available for applications per week.")
    else:
        st.write("No data available for applications per week.")

# Existing charts
col5, col6 = st.columns(2)

with col5:
    st.markdown('Articles Published Per Month')
    if articles_df is not None:
        if not articles_df.empty:
            articles_df['year_month'] = articles_df['year'].astype(str) + '-' + articles_df['month'].astype(str)
            articles_chart = articles_df.set_index('year_month')['article_count']
            st.bar_chart(articles_chart)
        else:
            st.write("No data available for articles published per month.")
    else:
        st.write("No data available for articles published per month.")

with col6:
    st.markdown('Users Joined Per Week')
    if users_df is not None:
        if not users_df.empty:
            users_df['year_week'] = users_df['year'].astype(str) + '-W' + users_df['week'].astype(str)
            users_chart = users_df.set_index('year_week')['user_count']
            st.line_chart(users_chart)
        else:
            st.write("No data available for users joined per week.")
    else:
        st.write("No data available for users joined per week.")

# Second row of existing charts
col7, col8 = st.columns(2)

with col7:
    st.markdown('Jobs Listed Per Week')
    if jobs_df is not None:
        if not jobs_df.empty:
            jobs_df['year_week'] = jobs_df['year'].astype(str) + '-W' + jobs_df['week'].astype(str)
            jobs_chart = jobs_df.set_index('year_week')['listing_count']
            st.bar_chart(jobs_chart)
        else:
            st.write("No data available for jobs listed per week.")
    else:
        st.write("No data available for jobs listed per week.")

with col8:
    st.markdown('Messages Sent Per Week')
    if messages_df is not None:
        if not messages_df.empty:
            messages_df['year_week'] = messages_df['year'].astype(str) + '-W' + messages_df['week'].astype(str)
            messages_chart = messages_df.set_index('year_week')['message_count']
            st.line_chart(messages_chart)
        else:
            st.write("No data available for messages sent per week.")
    else:
        st.write("No data available for messages sent per week.")

# Donut chart for Number of Users in Each Role
st.markdown('Distribution of Users in Each Role')
if roles_df is not None:
    if not roles_df.empty:
        fig = px.pie(
            roles_df,
            names='role',
            values='user_count',
            hole=0.4
        )
        st.plotly_chart(fig)
    else:
        st.write("No data available for user roles.")
else:
    st.write("No data available for user roles.")
