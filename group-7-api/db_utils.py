import mysql.connector
from config import HOST, USER, PASSWORD
import random

def _connect_to_db(db_name):
    try:
        cnx = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            auth_plugin='mysql_native_password',
            database=db_name
        )
        return cnx
    except Exception as e:
        print(f"Failed to connect to the database: {str(e)}")
        return None

# Function code - all called in options of menu in main.py
# Called in option 1 of run() menu in main.py
def get_all_books():
    """
    Retrieve a list of all available books with book ID, title, author, and price.

    Returns:
        list: A list of book records.
    """
    try:
        db_name = 'seventhHeaven'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to database {db_name}")

        # Query to retrieve a list of all available books, including book ID, title, author, and price
        query = """SELECT books.bookID, books.title, 
               CONCAT(authors.FirstName, ' ', authors.Surname) AS author,
               books.price
        FROM books
        INNER JOIN authors ON books.authorID = authors.authorID"""

        cur.execute(query)
        results = cur.fetchall()
        return results  # Return the results

    except Exception as exc:
        print(exc)
        return None  # Return None in case of an error

    finally:
        if db_connection:
            db_connection.close()


# called in option 1 of run() menu in main.py - if customer wishes to purchase book
def get_book_price(book_id):
    """
    Retrieve the price of a book by its ID.

    Args:
        book_id (int): The ID of the book for which you want to retrieve the price.

    Returns:
        float: The price of the book.
    """
    try:
        db_name = 'seventhHeaven'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to database {db_name}")

        # Query to retrieve the price of a book by its ID
        query = "SELECT price FROM books WHERE bookID = %s"

        cur.execute(query, (book_id,))
        result = cur.fetchone()

        if result:
            price = result[0]
            return price

    except Exception as exc:
        print(exc)
        return None  # Return None in case of an error

    finally:
        if db_connection:
            db_connection.close()


# called in option 1 of run() menu in main.py - updates stock in bookAvailability table
def update_book_stock(book_id, branch_id, new_stock_count):
    """
        Updates the stock count of a specific book in a branch.

        Args:
            book_id (int): The ID of the book to update.
            branch_id (int): The ID of the branch where the book is located.
            new_stock_count (int): The new stock count to set for the book in the branch.

        Returns:
            None
        """
    try:
        db_name = 'seventhHeaven'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()

        query = """
            UPDATE bookAvailability
            SET Stock = %s
            WHERE BookID = %s AND BranchID = %s
            """
        cur.execute(query, (new_stock_count, book_id, branch_id))
        db_connection.commit()
    except Exception as exc:
        print(exc)
    finally:
        if db_connection:
            db_connection.close()


# called in option 2 of run() menu in main.py
def get_genres():
    """
        Retrieve a list of genres available in the bookshop.

        Returns:
            list: A list of book genres
        """
    try:
        db_name = 'seventhheaven'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to database: {db_name}')

        # Query to retrieve a list of book genres for books stocked by the chain
        query = """
            SELECT GenreName
            FROM genres
        """
        cur.execute(query)
        results = [row[0] for row in cur.fetchall()]  # retrieve both GenreID and GenreName
        cur.close()
        return results

    except Exception as exc:
        print(exc)
        return None  # Return None in case of an error

    finally:
        if db_connection:
            db_connection.close()
            print("Connection closed")


def get_books_by_genre_name(genre_search):
    """
    Retrieve books with a genre name containing the genre_search.

    Args:
        genre_search (str): The partial genre name to search for.

    Returns:
        list: A list of books with matching genre names.
    """
    try:
        db_name = 'seventhHeaven'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to database: {db_name}')

        # Query to retrieve books with a genre name containing the genre_search
        query = """
        SELECT DISTINCT books.bookID, books.title, 
               CONCAT(authors.FirstName, ' ', authors.Surname) AS author,
               books.price
        FROM books
        INNER JOIN authors ON books.authorID = authors.authorID
        INNER JOIN genres ON books.genreID = genres.genreID
        WHERE genres.GenreName LIKE %s
        """
        cur.execute(query, (f"%{genre_search}%",))   #wildcard used for partial matching
        results = cur.fetchall()
        cur.close()
        return results

    except Exception as exc:
        print(exc)
        return None  # Return None in case of an error

    finally:
        if db_connection:
            db_connection.close()
            print("Connection closed")


# Called in option 3 of run() menu in main.py
def get_authors_records():
    """
        Retrieve a list of all available books with book ID, title, author, and price.

        Returns:
            list: A list of authors names
        """
    try:
        db_name = 'seventhHeaven'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connect to database: {db_name}')
        query = """SELECT concat(FirstName, ' ', Surname)  FROM authors"""
        cur.execute(query)
        results = cur.fetchall()
        return results



    except Exception as exc:

        print(exc)

        return None  # Return None in case of an error


    finally:

        if db_connection:
            db_connection.close()

            print("Connection closed")


def get_books_by_author_name(author_name):
    """
    Retrieve a list of books containing author_name.

    Args:
        author_name (str): The partial or full author name to search for.

    Returns:
        list: A list of book records.
    """

    try:
        db_name = 'seventhHeaven'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to database {db_name}")

        query = """
        SELECT books.bookID, books.title, CONCAT(authors.FirstName, ' ', authors.Surname) AS Author, books.price
        FROM books
        INNER JOIN authors ON books.authorID = authors.authorID
        WHERE CONCAT(authors.FirstName, ' ', authors.Surname) LIKE %s
        """

        cur.execute(query, (f'%{author_name}%',))  # Use % for wildcard matching
        results = cur.fetchall()
        return results

    except Exception as exc:
        print(exc)
        return None

    finally:
        if db_connection:
            db_connection.close()


# Called in option 4 of run() menu in main - all stock info
def get_book_stock_info():
    """
    Retrieve stock information for all books in all branches, including Book title and Branch location.

    Returns:
        list: A list of stock information records (BookID, Book Title, Branch Location, Stock)
    """
    try:
        db_name = 'seventhHeaven'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()

        query = """
        SELECT ba.BookID, b.Title, sb.Location, ba.Stock
        FROM bookAvailability AS ba
        JOIN books AS b ON ba.BookID = b.BookID
        JOIN storeBranch AS sb ON ba.BranchID = sb.BranchID
        """

        cur.execute(query)
        results = cur.fetchall()
        return results

    except Exception as exc:
        print("Error:", exc)  # debugging statement
        return None

    finally:
        if db_connection:
            db_connection.close()


# alternative function for check_book_availability
def check_book_availability(book_id, branch_id):
    try:
        db_name = 'seventhHeaven'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to database {db_name}")

        query = """
        SELECT Availability, Stock
        FROM bookAvailability
        WHERE BookID = %s AND BranchID = %s
        """ # %s placeholder for value supplied when query executed

        cur.execute(query, (book_id, branch_id))
        result = cur.fetchone()

        if result:
            availability, stock = result
            return(result)
        else:
            # Book not found in the specified branch
            return None

    except Exception as exc:
        print(exc)
        return None

    finally:
        if db_connection:
            db_connection.close()
def get_random_books(num_books=3):
    """
    Retrieve a list of random available books with book ID, title, author, and price.

    Args:
        num_books (int): The number of random books to retrieve.

    Returns:
        list: A list of random book records.
    """
    try:
        db_name = 'seventhHeaven'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to database {db_name}")

        # Query to retrieve a list of all available books, including book ID, title, author, and price
        query = """SELECT books.bookID, books.title, 
               CONCAT(authors.FirstName, ' ', authors.Surname) AS author,
               books.price
        FROM books
        INNER JOIN authors ON books.authorID = authors.authorID"""

        cur.execute(query)
        all_books = cur.fetchall()

        # Get a random sample of books
        random_books = random.sample(all_books, num_books)

        return random_books  # Return the random books

    except Exception as exc:
        print(exc)
        return None  # Return None in case of an error

    finally:
        if db_connection:
            db_connection.close()

def insert_donated_book(title, author, genre, condition, description):
    try:
        db_name = 'seventhHeaven'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()

        # SQL query to insert the donated book details into the database
        insert_query = """
            INSERT INTO donated_books (title, author, genre, `condition`, description)
            VALUES (%s, %s, %s, %s, %s)
        """
        data = (title, author, genre, condition, description)

        cur.execute(insert_query, data)
        db_connection.commit()


    except Exception as e:
        print(f"Failed to insert book donation: {str(e)}")

    finally:
        if db_connection:
            cur.close()
            db_connection.close()