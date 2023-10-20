import mysql.connector
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


def get_all_books():
    try:
        db_name = 'seventhHeaven'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to database {db_name}")

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
            return availability, stock
        else:
            # Book not found in the specified branch
            return None

    except Exception as exc:
        print(exc)
        return None

    finally:
        if db_connection:
            db_connection.close()
