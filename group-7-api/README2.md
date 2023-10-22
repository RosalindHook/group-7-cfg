This file will eventually become the documentation for how to run the API, including editing the config file, any installation requirements up until how to run the code and what is supposed to happen.

Question 2 - Design and implement a simple API as done in class. 

Group 7's planned scenario is managing a book shop.

Other requirements for this assignment are:

- [X] Implement API endpoints with appropriate functionality
- [ ] Implement one additional endpoint of your choice (can be POST or GET but with a different implementation)
- [X] Implement client-side for the 3 API endpoints
- [X] Create a MySQL database with at least 1 table
- [X] Have a config file (do not leave your private information here)
- [X] Have db_utils file and use exception handling
- [X] Use appropriate SQL queries to interact with the database in your Flask application, and demonstrate at least two different queries.
- [X] In main.py have a run() function/call the functions to simulate the planned interaction with the API, this could include welcome statements, displaying etc., (hairdressers booking example from lesson)
- [X] Have correct but minimal  imports per file (do not import things you do not use in the 
file)
- [ ] Document how to run your API in a markdown file including editing the config file, any installation requirements up until how to run the code and what is supposed to happen.
- [ ] Submit in GitHub as a Pull Request


# Code Queens' Bookshop API Documentation

This documentation provides an overview of the Code Queens' Bookshop API, which includes Python code and a MySQL database for a bookshop management system for the "Seventh Heaven" Bookshop and its multiple branches. 
The API allows users to browse books, explore various genres and authors, get bonus book offers and donate books. 

### **Table of Contents**

1. Configuration
2. Installation Requirements
3. Running the Code
4. API Endpoints
5. GET /authors
6. GET /books
7. POST /buy-book
8. GET /stock
9. GET /bonus
10. Database
11. Usage

### Configuration
Before running the Code Queens' Bookshop API, you need to configure the database connection in the config.py file. Replace the following placeholders with your database information:
``````
HOST = "X"  # Replace with your MySQL server host
USER = "X"  # Replace with your MySQL username
PASSWORD = "X"  # Replace with your MySQL password
``````
Different team members can use their own config.py files with their own configuration settings, allowing each member to work with the database without affecting the main code.

### Installation Requirements 
Install the following:

- Python 3.x
- Flask
- MySQL server

#