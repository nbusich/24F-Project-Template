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
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data from {endpoint}: {e}")
        return None

# Set the page title
st.title('Database Analytics Dashboard')

# Fetch data for new metrics
avg_query_time_data = fetch_data('average_query_execution_time')
number_of_connections_data = fetch_data('number_of_connections')
database_uptime_data = fetch_data('database_uptime')
number_of_slow_queries_data = fetch_data('number_of_slow_queries')
table_sizes_data = fetch_data('table_sizes')
table_row_counts_data = fetch_data('table_row_counts')

# Display metrics
col1, col2, col3 = st.columns(3)

with col1:
    avg_time = 'N/A'
    if avg_query_time_data:
        if isinstance(avg_query_time_data, list) and len(avg_query_time_data) > 0:
            avg_time = avg_query_time_data[0].get('average_query_execution_time_ms', 'N/A')
        elif isinstance(avg_query_time_data, dict):
            avg_time = avg_query_time_data.get('average_query_execution_time_ms', 'N/A')
    st.metric(label="Average Query Time (ms)", value=avg_time)

with col2:
    num_connections = 'N/A'
    if number_of_connections_data:
        if isinstance(number_of_connections_data, list) and len(number_of_connections_data) > 0:
            num_connections = number_of_connections_data[0].get('number_of_connections', 'N/A')
        elif isinstance(number_of_connections_data, dict):
            num_connections = number_of_connections_data.get('number_of_connections', 'N/A')
    st.metric(label="Number of Connections", value=num_connections)

with col3:
    uptime_hours = 'N/A'
    if database_uptime_data:
        if isinstance(database_uptime_data, list) and len(database_uptime_data) > 0:
            uptime_seconds = int(database_uptime_data[0].get('database_uptime_seconds', 0))
        elif isinstance(database_uptime_data, dict):
            uptime_seconds = int(database_uptime_data.get('database_uptime_seconds', 0))
        else:
            uptime_seconds = 0
        uptime_hours = round(uptime_seconds / 3600, 2)
    st.metric(label="Database Uptime (hours)", value=uptime_hours)

# Second row of metrics
col4, col5 = st.columns(2)

with col4:
    slow_queries = 'N/A'
    if number_of_slow_queries_data:
        if isinstance(number_of_slow_queries_data, list) and len(number_of_slow_queries_data) > 0:
            slow_queries = number_of_slow_queries_data[0].get('number_of_slow_queries', 'N/A')
        elif isinstance(number_of_slow_queries_data, dict):
            slow_queries = number_of_slow_queries_data.get('number_of_slow_queries', 'N/A')
    st.metric(label="Number of Slow Queries", value=slow_queries)

with col5:
    # Calculate total database size
    if table_sizes_data:
        if isinstance(table_sizes_data, list):
            total_db_size = sum(float(item['size_mb']) for item in table_sizes_data)
            st.metric(label="Database Size (MB)", value=round(total_db_size, 2))
        else:
            st.metric(label="Database Size (MB)", value='N/A')
    else:
        st.metric(label="Database Size (MB)", value='N/A')

# Display table sizes
if table_sizes_data and isinstance(table_sizes_data, list) and len(table_sizes_data) > 0:
    table_sizes_df = pd.DataFrame(table_sizes_data)
    fig = px.bar(table_sizes_df, x='TABLE_NAME', y='size_mb', title='Table Sizes')
    st.plotly_chart(fig)
else:
    st.write("No data available for table sizes.")

# Display number of rows per table
if table_row_counts_data and isinstance(table_row_counts_data, list) and len(table_row_counts_data) > 0:
    table_row_counts_df = pd.DataFrame(table_row_counts_data)
    fig = px.bar(table_row_counts_df, x='TABLE_NAME', y='TABLE_ROWS', title='Rows per Table')
    st.plotly_chart(fig)
else:
    st.write("No data available for table row counts.")
