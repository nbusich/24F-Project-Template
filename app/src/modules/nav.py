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


#### ------------------------ Examples for Role of pol_strat_advisor ------------------------
def PolStratAdvHomeNav():
    st.sidebar.page_link(
        "pages/00_Pol_Strat_Home.py", label="Political Strategist Home", icon="👤"
    )


def WorldBankVizNav():
    st.sidebar.page_link(
        "pages/01_World_Bank_Viz.py", label="World Bank Visualization", icon="🏦"
    )


def MapDemoNav():
    st.sidebar.page_link("pages/02_Map_Demo.py", label="Map Demonstration", icon="🗺️")


## ------------------------ Examples for Role of usaid_worker ------------------------
def ApiTestNav():
    st.sidebar.page_link("pages/12_API_Test.py", label="Test the API", icon="🛜")


def PredictionNav():
    st.sidebar.page_link(
        "pages/11_Prediction.py", label="Regression Prediction", icon="📈"
    )


def ClassificationNav():
    st.sidebar.page_link(
        "pages/13_Classification.py", label="Classification Demo", icon="🌺"
    )


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
    st.sidebar.page_link("pages/22_Student_Home.py", label="Student Dashboard", icon="🗂️")

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app.
    Users do not need to be authenticated for the sidebar to show links.
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

    elif user_role == "Administrator"
        AdminDash()
        AdminChange()
        AdminUsage()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
