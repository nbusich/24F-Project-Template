import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks
import plotly.express as px
import matplotlib.pyplot as plt

########################################################################
# $$ average_query_execution_time
# $$ number_of_slow_queries
# $$ number_of_connections
# $$ database_uptime
# $$ table_sizes
# $$ table_row_counts
#########################################################################

# Base URL for your API
BASE_URL = 'http://api:4000/admin'
SideBarLinks()
st.header("**Database Analytics**")
col1, col2 = st.columns(2)


# Function to fetch data from API endpoints
def fetch_data(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data from {endpoint}: {e}")
        return None


# Fetch data for new metrics
avg_query_time_data = fetch_data('average_query_execution_time')
number_of_connections_data = fetch_data('number_of_connections')
database_uptime_data = fetch_data('database_uptime')
number_of_slow_queries_data = fetch_data('number_of_slow_queries')
table_sizes_data = fetch_data('table_sizes')
table_row_counts_data = fetch_data('table_row_counts')

with col1:
    with st.container(height = 180, border = True):
        st.write("##### Query Metrics")

        response = requests.get('http://api:4000/admin/average_query_execution_time').json()
        df = pd.DataFrame(response)
        st.write(f"**Average SELECT Execution Time**: {df['avg_exec_time_ms'][0]} ms")


        response = requests.get('http://api:4000/admin/number_of_slow_queries').json()
        df = pd.DataFrame(response)
        st.write(f"**Number of Slow Queries**: {df['Value'][0]}")

        response = requests.get('http://api:4000/admin/dashboard').json()
        df = pd.DataFrame(response)
        st.write(f"**Number of Queries Run**: {df['Value'][0]}")

with col2:
    with st.container(height=180, border=True):
        st.write("##### Database Metrics")

        response = requests.get('http://api:4000/admin/number_of_connections').json()
        df = pd.DataFrame(response)
        st.write(f"**Connected Threads**: {df['Value'][0]}")

        response = requests.get('http://api:4000/admin/database_uptime').json()
        df = pd.DataFrame(response)
        st.write(f"**Database Uptime**: {df['Value'][0]} seconds")

        # Calculate total database size
        if table_sizes_data:
            if isinstance(table_sizes_data, list):
                total_db_size = sum(float(item['size_mb']) for item in table_sizes_data)
                st.write(f"**Database Size**: {round(total_db_size, 2)} (MB)")
            else:
                st.metric(label="Database Size (MB)", value='N/A')
        else:
            st.metric(label="Database Size (MB)", value='N/A')




response = requests.get('http://api:4000/admin/average_query_execution_time').json()
df = pd.DataFrame(response)
fig = px.bar(
    df,
    x='EVENT_NAME',
    y='avg_exec_time_ms',
    color='EVENT_NAME',
    title="Average Execution Time (ms)",
    labels={
        "EVENT_NAME": "Event Type",  # Custom x-axis title
        "avg_exec_time_ms": "Execution Time (ms)" # Custom y-axis title
    },
    width=400,
    height=400
)
with st.container(height=450, border=True):
    st.plotly_chart(fig, use_container_width=True, on_select="rerun")



with st.container(height=500, border=True):
    # Display table sizes
    if table_sizes_data and isinstance(table_sizes_data, list) and len(table_sizes_data) > 0:
        table_sizes_df = pd.DataFrame(table_sizes_data)
        fig = px.bar(table_sizes_df, x='TABLE_NAME', y='size_mb', title='Table Sizes')
        st.plotly_chart(fig)
    else:
        st.write("No data available for table sizes.")
with st.container(height=500, border=True):
    # Display number of rows per table
    if table_row_counts_data and isinstance(table_row_counts_data, list) and len(table_row_counts_data) > 0:
        table_row_counts_df = pd.DataFrame(table_row_counts_data)
        fig = px.bar(table_row_counts_df, x='TABLE_NAME', y='TABLE_ROWS', title='Rows per Table')
        st.plotly_chart(fig)
    else:
        st.write("No data available for table row counts.")
