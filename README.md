# Fall 2024 CS 3200 CoffeeStats Repository

Welcome to CoffeeStats! 

    CoffeeStats is a web application for viewing and understanding important statistics about co-ops and encouraging communication between the different parties involved in finding a co-op match. 
    

    - All authenticated users have access to an explore page where they can see all the job listings. Clicking one brings you to its individual listing page.
    
    - Co-op Advisors can see information about current applications, students, what co-ops might be a good match for them, as well as matching them with a peer to encourage a 'Coffee Chat'. 
    
    - Alumni can set up profiles that demonstrate their previous experience, along with contact information to encourage undergrads to reach out. 
    
    - HR Contacts can create job listings, linking any number of relevant majors and relevant fields. They have access to a page of just their own listings, where they can chose to edit or delete an existing listing.

    - Students can view helpful links associated with the co-op process, and connect with their advisor, a peer mentor, or an alumnus.

    - System Administrators can see info relating to the backend of the app, with database analytics as well as usage statistics for the app itself. They maintain a changelog, allowing them to create and view change documentation.

Video Demo: https://youtu.be/Roib-zIwDv4

For information about the structure of this repo and how to get the application to spin up on your computer, read below!


## Current Project Components

Currently, there are three major components which will each run in their own Docker Containers:

- Streamlit App in the `./app` directory
- Flask REST api in the `./api` directory
- SQL files for your data model and data base in the `./database-files` directory

### Setting Up Your Personal Repo

1. In GitHub, click the **fork** button in the upper right corner of the repo screen. 
1. When prompted, give the new repo a unique name, perhaps including your last name and the word 'personal'. 
1. Once the fork has been created, clone YOUR forked version of the repo to your computer. 
1. Set up the `.env` file in the `api` folder based on the `.env.template` file.
1. Start the docker containers. 

## Controlling the Containers

- `docker compose up -d` to start all the containers in the background
- `docker compose down` to shutdown and delete the containers
- `docker compose up db -d` only start the database container (replace db with the other services as needed)
- `docker compose stop` to "turn off" the containers but not delete them. 


