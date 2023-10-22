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


## Table of contents
1. [Configuration](#Configuration)
2. [Installation Requirements](#Installation-requirements)
3. [Running the Code](#Running-the-code)
4. [App File](#App)
5. [Database Utilities File](#db-util)
6. [Main Application](#main)
7. [MySQL Database](#Database)
8. [API Endpoints](#API-endpoints)
    1. [GET /authors](#authors)
   2. [GET /books](#books)
   3. [POST /buy-book](#buy-book)
   4. [GET /stock](#stock)
   5. [GET /bonus](#bonus)
   6. [POST /donation](#donation)
9. [Usage](#Usage)



### Configuration <a name="Configuration"></a>
Before running the Code Queens' Bookshop API, you need to configure the database connection in the config.py file. Replace the following placeholders with your database information:
``````
HOST = "X"  # Replace with your MySQL server host
USER = "X"  # Replace with your MySQL username
PASSWORD = "X"  # Replace with your MySQL password
``````
Different team members can use their own config.py files with their own configuration settings, allowing each member to work with the database without affecting the main code.


### Installation Requirements <a name="Installation-requirements"></a>
Install the following:

- Python 3.x
- Flask
- MySQL server


### Running the Code <a name="Running-the-code"></a>
- Create and configure the config.py file as described in the Configuration section.
- Ensure that your MySQL server is running.
- Run the Flask application by executing the following command in your terminal:
``````
python app.py
``````
- The API will start running on http://127.0.0.1:5003 (the endpoints can be accessed via this URL)


### App File <a name="App"></a>


### Database Utilities File <a name="db_util"></a>


### Main Application <a name="main"></a>


### MySQL Database <a name="Database"></a>
The API interacts with a MySQL database named "seventhHeaven". 
The database contains tables for books, authors, genres, store branches, store owners, and book availability. 
The tables are populated with sample data.

### API Endpoints <a name="API-endpoints"></a>

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


### Usage <a name="Usage"></a>
This API is designed to be used by the Seventh Heaven Bookshop. 
Cusotmers can  interact with the bookshop through the API and perform various actions.

**Usage steps :**
1. Start the API by running the file 'app.py'.
2. Access the API endpoints to browse books, explore genres and authors, make purchases, get bonus book offers and donate books.



