##################################################
# Useful Student Links
##################################################

import streamlit as st

def UsefulStudentLinks():
    """
    Displays helpful links for students in a nicely formatted way.
    """
    st.sidebar.write("### Useful Links")
    st.sidebar.write("Here are some quick access resources for Northeastern students:")
    
    links = {
        "Northeastern Co-op Portal": "https://northeastern-csm.symplicity.com/students/?signin_tab=0",
        "Academic Calendar": "https://registrar.northeastern.edu/calendar",
        "Student Support Services": "https://studentlife.northeastern.edu/",
        "Career Development Resources": "https://careers.northeastern.edu/",
        "University Libraries": "https://library.northeastern.edu/",
    }

    for label, url in links.items():
        st.sidebar.markdown(f"- [{label}]({url})")