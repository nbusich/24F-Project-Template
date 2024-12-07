import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    Welcome to CoffeeStats! 

    CoffeeStats is a web application for viewing and understanding important statistics about co-ops and encouraging communication between the different parties involved in finding a co-op match. 
    

    - All authenticated users have access to an explore page where they can see all the job listings. Clicking one brings you to its individual listing page.
    
    - Co-op Advisors can see information about current applications, students, what co-ops might be a good match for them, as well as matching them with a peer to encourage a 'Coffee Chat'. 
    
    - Alumni can set up profiles that demonstrate their previous experience, along with contact information to encourage undergrads to reach out. 
    
    - HR Contacts can create job listings, linking any number of relevant majors and relevant fields. They have access to a page of just their own listings, where they can chose to edit or delete an existing listing.

    - Students can view helpful links associated with the co-op process, and connect with their advisor, a peer mentor, or an alumnus.

    - System Administrators can see info relating to the backend of the app, with database analytics as well as usage statistics for the app itself. They maintain a changelog, allowing them to create and view change documentation.


    """
        )
