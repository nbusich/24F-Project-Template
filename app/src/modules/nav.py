# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")

def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="ℹ️")

def ExploreListingsNav():
    st.sidebar.page_link("pages/17_All_Listings.py", label="Explore Listings", icon="🚀")

#### ------------------------ System Admin Role ------------------------
def AdminDash():
    st.sidebar.page_link(
        "pages/A1_admin_home.py", label="Dashboard", icon="📊"
    )
def AdminChange():
    st.sidebar.page_link(
        "pages/A2_admin_changes.py", label="Changes", icon="✏️"
    )
def AdminUsage():
    st.sidebar.page_link(
        "pages/A3_admin_analytics.py", label="Usage Analytics", icon="📈"
    )
#### ------------------------ HR Contact Role ------------------------
def CompanyNav():
    st.sidebar.page_link("pages/14_Company_Home.py", label="Company Home", icon="👤")

#### ------------------------ Student Role ------------------------
def StudentDash():
    st.sidebar.page_link("pages/22_Student_Home.py", label="Return To Dashboard", icon="🏠")

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] {
                width: 250px;  /* Adjust sidebar width */
                min-width: 250px; /* Ensure it doesn't shrink below this width */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # add a logo to the sidebar always
    st.sidebar.image("assets/Coffee_stats_logo.png", width=200)

    # Allow the user to select their role (replaces the need for authentication)
    user_role = st.sidebar.selectbox("Select your role", ["Student", "Alumnus", "Administrator", "Advisor", "Company"])

    # Links for all users
    HomeNav()
    ExploreListingsNav()

    # Show links based on the selected role
    if user_role == "Student":
        StudentDash()
        st.sidebar.write("### Student Links")
        st.sidebar.write("""
        - [Northeastern Co-op Portal](https://northeastern-csm.symplicity.com/students/?signin_tab=0)
        - [Academic Calendar](https://registrar.northeastern.edu/calendar)
        - [Student Support Services](https://studentlife.northeastern.edu/)
        """)

    elif user_role == "Company":
        CompanyNav()

    elif user_role == "Administrator":
        AdminDash()
        AdminChange()
        AdminUsage()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()