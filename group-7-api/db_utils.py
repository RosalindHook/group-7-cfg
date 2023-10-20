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

def get_authors_records():
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
get_authors_records()
# guery for store procedure. Check if book available, which store, price by title name of book
def find_book_availability(book_title):
    try:
        db_name = 'seventhheaven'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        print(f'Connect to database: {db_name}')
        #Execute the stored procedure using a SQL query
        query = "CALL FindBookAvailability(%s)"
        cursor.execute(query, (book_title,))
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
# Example usage:
book_title = "The Hobbit"
availability_info = find_book_availability(book_title)

if availability_info:
    for book_info in availability_info:
        print(f"Book: {book_info['BookTitle']}, Branch: {book_info['StoreBranch']}, Availability: {book_info['IsAvailable']}, Price: {book_info['BookPrice']}")