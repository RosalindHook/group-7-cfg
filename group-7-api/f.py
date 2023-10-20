import mysql.connector

def find_book_availability(book_title):
    try:
        # Replace these with your database credentials
        db_config = {
            "host": "Localhost",
            "user": "Olga",
            "password": "Hj,jnf23",
            "database": "seventhHeaven"  # Your database name
        }

        # Connect to the MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Execute the stored procedure using a SQL query
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
        conn.close()

# Example usage:
book_title = "Harry Potter and the Philosophers Stone"
availability_info = find_book_availability(book_title)

if availability_info:
    for book_info in availability_info:
        print(f"Book: {book_info['BookTitle']}, Branch: {book_info['StoreBranch']}, Availability: {book_info['IsAvailable']}, Price: {book_info['BookPrice']}")