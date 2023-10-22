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

---
## Table of contents
1. [Scenario](#scenario)
2. [Installation Requirements](#installation)
3. [Configuration](#config)
4. [Running the Code](#running-code)
5. [App File](#App)
9. [API Endpoints](#api)
    1. [GET /authors](#authors)
   2. [GET /books](#books)
   3. [POST /buy-book](#buy-book)
   4. [GET /stock](#stock)
   5. [GET /bonus](#bonus)
   6. [POST /donation](#donation)
6. [Database Utilities File](#util)
7. [Main Application](#main)
8. [MySQL Database](#database)
10. [Usage](#usage)



---
## Scenario <a name="scenario"></a>
The Code Queens have opened a chain of bookshops, Seventh Heaven, with branches in Edinburgh, Glasgow, London and Sutton. 


We have built a web application using Flask, to provide a user-friendly experience for book enthusiasts.
This application enables customers to browse an extensive collection of books, explore genres and authors, and receive bonus book recommendations with discounts.


Customers are able to make purchases across multiple branch locations, with a discount of 10% applied for purchases of 3 or more books. 
We also have an exciting feature whereby customers are able to donate books to the branch of their choice.


Explore our digital bookshelves and embark on a literary journey with the Code Queens’ Seventh Heaven Bookshop. 


Enjoy book browsing!

---
## Installation Requirements <a name="installation"></a>
**Install the following:**

- Python 3.x
- Flask
- MySQL server

---
## Configuration <a name="config"></a>
Before running the Code Queens' Bookshop API, you need to configure the database connection in the config.py file - this ensure that the application can connect to your specific database.

Replace the following placeholders with your database information:
``````
HOST = "X"  # Replace with your MySQL server host
USER = "X"  # Replace with your MySQL username
PASSWORD = "X"  # Replace with your MySQL password
``````
Different team members can use their own config.py files with their own configuration settings, allowing each member to work with the database without affecting the main code.


---
## Running the Code <a name="running-code"></a>
**Steps to run the application:**

1. Clone the repository 
   - Start by cloning the repository from the ‘group-7-api’ folder on Github. 
   - Create a new project folder in your local repository.
2. Activate a virtual environment 
   - Navigate to your project folder and activate a virtual environment. This ensures a clean and isolated environment for the application.
3. Install the required modules in your virtual environment using pip
   - **Requests module** - used for making HTTP requests
   - **Mysql-connector-python** - used for connecting to a MySQL database and executing SQL queries. 
   - **Flask** - used to run the Flask web application in ‘app.py’
   - Other modules and files that need to be imported are listed at the top of each file - these do not require separate installation, as they include built-in Python modules, project-specific files or modules that are automatically imported as part of the code.
4. Configure the database connection 
   - In the ‘config.py’ file, replace the ‘X’ placeholder information with your own MySQL Workbench database connection details *(see configuration section for more info).*
5. Database setup
   - Open ‘bookshop.sql’ using MySQL workbench. 
   - Use the SQL script to create the database named ‘seventhHeaven’ and the necessary tables - this step is essential to store and retrieve bookshop data effectively.
6. Run app.py to start the Flask web application. Make sure it is successfully connected to a server.
7. Then execute main.py, and you'll be greeted with a user-friendly menu to access a range of book browsing options.


API endpoints can be accessed via this URL: http://127.0.0.1:5003 

---
## App File <a name="App"></a>
The **App.py file** handles the core functionality and interaction with the database.

### API Endpoints <a name="api"></a>


#### GET /authors <a name="authors"></a>
- Retrieves a list of all authors available in the bookstore.
- URL: http://127.0.0.1:5003/authors

#### GET /books  <a name="books"></a>
- Retrieves a list of all available books with details including Book ID, Title, Author, and Price.
- URL: http://127.0.0.1:5003/books

#### POST /buy-book <a name="buy-book"></a>
- Allows customers to purchase a book by specifying the Book ID and the Branch ID they want to buy it from.
- URL: http://127.0.0.1:5003/buy-book

#### GET /stock  <a name="stock"></a>
- Retrieves stock information for all books in all branches, including Book ID, Book Title, Branch Location, and Stock count.
- URL: http://127.0.0.1:5003/stock

#### GET /bonus  <a name="bonus"></a>
- Provides a list of random bonus book offers. Customers can choose a book from the list and get it at a discounted price.
- URL: http://127.0.0.1:5003/bonus

#### POST /donation <a name="donation"></a>
- Allows customers to donate a used book to the bookshop.
- URL: 


---
### Database Utilities File <a name="util"></a>

---
### Main Application <a name="main"></a>

---
### MySQL Database <a name="database"></a>
The API interacts with a MySQL database named "seventhHeaven". 
The database contains tables for books, authors, genres, store branches, store owners, and book availability. 
The tables are populated with sample data.

---
### Usage <a name="usage"></a>
This API is designed to be used by the Seventh Heaven Bookshop. 
Cusotmers can  interact with the bookshop through the API and perform various actions.

**Usage steps :**
1. Start the API by running the file 'app.py'.
2. Access the API endpoints to browse books, explore genres and authors, make purchases, get bonus book offers and donate books.



