##################################################
# Useful Student Links
##################################################

import streamlit as st

def display_student_links():
    st.title("Helpful Links for Students")

    links = {
        "Northeastern Co-op Portal": "https://northeastern-csm.symplicity.com/students/?signin_tab=0",
        "Academic Calendar": "https://registrar.northeastern.edu/calendar",
        "Student Support Services": "https://studentlife.northeastern.edu/",
        "Career Development Resources": "https://careers.northeastern.edu/",
        "University Libraries": "https://library.northeastern.edu/",
        "Health and Counseling Services": "https://www.northeastern.edu/uhcs/",
        "Student Clubs and Organizations": "https://northeastern.presence.io/",
    }

    for label, url in links.items():
        st.markdown(f"- [{label}]({url})")

    st.write("\n")

if __name__ == "__main__":
    display_student_links()