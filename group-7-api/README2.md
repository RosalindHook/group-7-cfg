# Code Queens' Bookshop API Documentation :books:

This documentation provides an overview of the Code Queens' Bookshop API, which includes Python code and a MySQL database for a bookshop management system for the "Seventh Heaven" Bookshop and its multiple branches. 
The API allows users to browse books, explore various genres and authors, get bonus book offers and donate books. 

---
## Table of contents
1. [Scenario](#scenario)
2. [Installation Requirements](#installation)
3. [Configuration](#config)
4. [Running the Code](#running-code)
5. [App File](#App)
6. [API Endpoints](#api)
    1. [get_authors()](#authors)
   2. [get_books()](#books)
   3. [buy_book()](#buy-book)
   4. [get_stock_info()](#stock)
   5. [get_bonus()](#bonus)
   6. [donate_book()](#donation)
7. [Database Utilities File](#util)
8. [Main Application](#main)
9. [MySQL Database](#database)
10. [Usage](#usage)



---
## Scenario :clipboard: <a name="scenario"></a>
The Code Queens have opened a chain of bookshops, Seventh Heaven, with branches in Edinburgh, Glasgow, London and Sutton. 


We have built a web application using Flask, to provide a user-friendly experience for book enthusiasts.
This application enables customers to browse an extensive collection of books, explore genres and authors, and receive bonus book recommendations with discounts.


Customers are able to make purchases across multiple branch locations, with a discount of 10% applied for purchases of 3 or more books. 
We also have an exciting feature whereby customers are able to donate books to the branch of their choice.


Explore our digital bookshelves and embark on a literary journey with the Code Queens’ Seventh Heaven Bookshop. 


Enjoy book browsing!

---
## Installation Requirements :hammer_and_wrench:  <a name="installation"></a>
**Install the following:**

- Python 3.x
- Flask
- MySQL server

---
## Configuration :gear: <a name="config"></a>
Before running the Code Queens' Bookshop API, you need to configure the database connection in the config.py file - this ensure that the application can connect to your specific database.

Replace the following placeholders with your database information:
``````
HOST = "X"  # Replace with your MySQL server host
USER = "X"  # Replace with your MySQL username
PASSWORD = "X"  # Replace with your MySQL password
``````
Different team members can use their own config.py files with their own configuration settings, allowing each member to work with the database without affecting the main code.


---
## Running the Code :running: <a name="running-code"></a>
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
## App File :open_file_folder: <a name="App"></a>
The **App.py file** serves as the core of the Code Queens' Bookshop API. 

It is responsible for handling the fundamental functionality of the application and acts as the interface between the user and the database.

### API Endpoints <a name="api"></a>


#### get_authors() <a name="authors"></a>
- Handles GET requests to the '/authors' route, providing a list of authors' records from the database as JSON.
- URL: http://127.0.0.1:5003/authors

#### get_books() <a name="books"></a>
- Manages GET requests to the '/books' route, returning a list of all books as JSON.
- URL: http://127.0.0.1:5003/books

#### buy_book() <a name="buy-book"></a>
- Creates an endpoint for POST requests to the '/buy-book' route, allowing customers to purchase books with availability checks and stock updates.

#### get_stock_info()  <a name="stock"></a>
- Deals with GET requests to the '/stock' route, retrieving stock information for all books and branches.
- URL: http://127.0.0.1:5003/stock

#### get_bonus()  <a name="bonus"></a>
- Provides bonus book recommendations through GET requests to the '/bonus' route.
- URL: http://127.0.0.1:5003/bonus

#### donate_book() <a name="donation"></a>
- Allows customers to donate used books to the second-hand section of the bookshop.


---
### Database Utilities File :oil_drum: <a name="util"></a>
The **Db_utils.py file** is a collection of functions used to interact with the database.

These include:
1. **connect_to_db(db_name)**
   - Establishes a database connection and returns the connection object.
2. **get_all_books()**
   - Retrieves a list of available books, including book ID, title, author, and price.
3. **get_book_price(book_id)**
   - Retrieves a book's price based on its ID.
4. **update_book_stock(book_id, branch_id, new_stock_count)**
   - Updates the stock count for a specific book in a branch.
5. **get_genres()** 
   - Retrieves available book genres.
6. **get_books_by_genre_name(genre_search)**
   - Retrieves books matching a genre name.
7. **get_authors_records()**
   - Retrieves a list of all authors' names.
8. **get_books_by_author_name(author_name)**
   - Retrieves books by a specific author.
9. **get_book_stock_info()**
   - Retrieves stock information for all books in all branches.
10. **check_book_availability(book_id, branch_id)**
    - Checks book availability and stock in a branch.
11. **get_random_books(num_books=3)**
    - Retrieves a list of random available books.
12. **insert_donated_book(title, author, genre, condition, description)**
    - Inserts user data about used books.


---
### Main Application :iphone: <a name="main"></a>
The **main.py file** is the central script of Code Queens' Seventh Heaven Bookshop. 

This script offers several user-friendly features, allowing customers to browse, buy, explore genres and authors, and even receive bonus book recommendations with discounts. 

Once the application is up and running, simply execute main.py, and you'll be greeted with a user-friendly menu to access the following features:

1. **Browse Books:** The browse_books() function establishes a connection to the bookshop's backend through HTTP requests. 
   - It retrieves a list of available books from the database (using GET endpoint) and displays them in a clear format. 
   - Customers can view book titles, authors, and prices.
2. Customers then have the option to **buy a book** or return to the main menu. 
   - If they choose to make a purchase, the script guides them to the buying functionality (the buy_book() function), allowing customers to choose books and branch. 
   - It verifies the availability and stock of a specific book in a chosen branch. 
   - If the book is in stock, it updates the customer’s basket and adjusts the stock accordingly (using POST endpoint). 
   - When a customer buys three or more books, they are rewarded with a 10% discount.
3. **Explore genres and authors:** the explore_genres() and explore_authors() functions allow customers to explore books by either genre or author.
   - It provides a list of all genres or authors stocked by Seventh Heaven. 
   - Customers can then search for specific genres or authors and discover the matching books in the bookshop’s catalogues.
4. **Random bonus:** The random_bonus() function treats customers by fetching a random selection of books from the database (GET endpoint). 
   - Customers have the option to purchase these bonus books at a discounted price.
5. **Donate books:** The donate_book() function allows users to add data about books they would like to donate to the secondhand section of the bookshop. 
   - Customers can add a title, author, genre, condition and description of the book.

---
### MySQL Database :file_cabinet: <a name="database"></a>
The **bookshop.sql file** contains the database named "seventhHeaven". 

This database is designed to store and manage data related to books, authors, genres, store branches, and book availability.

Below is an overview of the tables in the database:

1. **Books**: Contains information about all the books available in the bookshop, including details like book ID, title, author, and price.
2. **Authors**: Stores data about authors, enabling customers to explore books by their favorite writers.
3. **Genres**: Provides information about different book genres, making it easier for customers to discover books in their preferred categories.
4. **Store Branches**: Contains data related to the different branches of Seventh Heaven bookshops in Edinburgh, Glasgow, London, and Sutton.
5. **Store Owners**: Maintains records of store owners who manage each branch.
6. **Book Availability**: Tracks the availability and stock of each book in every branch. This data is used to ensure customers can purchase books that are in stock.
7. **Donations**: An empty table that gets populated with data about books which customers would like to donate.

The tables are pre-populated with sample data (except the donations table) to demonstrate the functionality of our API. You can modify, extend, or populate these tables with your own data as needed.


---
### Usage :rocket: <a name="usage"></a>
The Code Queens' Bookshop API is designed for use by the Seventh Heaven Bookshop customers and provides a user-friendly and interactive experience. 

Below are the steps to use the API:

1. **Start the API**: Run the 'app.py' file to start the API. This action initializes the web application, and you can access the API endpoints to interact with the bookshop.
2. **Browse Books**: Use the API endpoints to browse a wide selection of books available in the bookshop. This includes viewing book titles, authors, and prices.
3. **Explore Genres and Authors**: The API provides functionality to explore books by genres and authors. You can discover books that match specific genres or authors and explore the bookshop's catalog.
4. **Make Purchases**: Customers can use the API to purchase books from different branches. The API checks book availability, and when customers buy three or more books, they receive a 10% discount on their purchase.
5. **Get Bonus Book Offers**: The API offers a feature to receive random bonus book recommendations at discounted prices. Customers can choose to buy these bonus books.
6. **Donate Books**: Customers can use the API to donate used books to the bookshop, making it easy for them to contribute to the bookshop's collection.

With these features, the Code Queens' Bookshop API provides a comprehensive tool for managing and enhancing the book-buying experience. 
Customers can explore, purchase, and contribute to the bookshop through a user-friendly interface.

**We hope you enjoy using the Code Queens' Bookshop API!**

