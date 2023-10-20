import mysql.connector
from mysql.connector import cursor
from config import HOST, USER, PASSWORD

def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


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


# TODO function to include a query to retrieve genres - to be called in option 2 of run() menu of main.py


# Called in option 3 of run() menu in main.py
def get_authors_records():
    """
        Retrieve a list of author names by combining their first name and surname.

        Returns:
            list: A list of author names.
        """
    try:
        db_name = 'seventhheaven'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connect to database: {db_name}')
        query = """SELECT concat(FirstName, ' ', Surname)  FROM authors"""
        cur.execute(query)
        results = cur.fetchall()

        for i in results:
            print (i)
        cur.close()
    except Exception:
        print("Failed to read data from database")
    finally:
        if db_connection:
            db_connection.close()
            print("Connection closed")


# guery for store procedure. Check if book available, which store, price by title name of book
def find_book_availability(book_id, branch_id):
    """
    Check if a book is available at a specific branch and return its details.

    Args:
        book_id (int): The ID of the book.
        branch_id (int): The ID of the branch.

    Returns:
        list: A list of book availability details.
    """
    try:
        db_name = 'seventhheaven'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        print(f'Connect to database: {db_name}')
        #Execute the stored procedure using a SQL query
        query = "CALL FindBookAvailability(%s, %s)"
        cursor.execute(query, (book_id, branch_id))
        # Retrieve the results
        results = []
        for row in cursor.fetchall():
            book_title, store_branch, availability, price = row
            results.append({
                "BookTitle": book_title,
                "StoreBranch": store_branch,
                "IsAvailable": availability,
                "BookPrice": price
            })

        return results
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
    finally:
        cursor.close()
        db_connection.close()
        print("Connection closed")
