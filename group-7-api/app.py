from flask import Flask, jsonify #, request   placeholder as not yet used
from db_utils import get_authors_records, get_all_books

app = Flask(__name__)
@app.route('/authors')
def get_authors():
    result = get_authors_records()
    return jsonify(result)


@app.route('/books', methods=['GET'])
def get_books():
    books = get_all_books()
    if books:
        books_data = [
            {
                "BookID": book_id,
                "Title": title,
                "Author": author,
                "Price": price
            }
            for book_id, title, author, price in books
        ]
        return jsonify(books_data)
    else:
        return jsonify([])  # if no books found, return empty list


@app.route('/buy-book', methods=['POST'])
def buy_book():
    book_data = request.json  # Get book information from the POST request in main.py

    book_id = book_data.get("book_id")
    branch_id = book_data.get("branch_id")

    # Check book availability and stock
    availability_result, stock = db_utils.check_book_availability(book_id, branch_id)

    if availability_result:
        if stock > 0:
            # Update the stock in your database (decrease stock count by 1)
            db_utils.update_book_stock(book_id, branch_id, stock - 1)

            # Record the purchase by inserting a record into the databse
            db_utils.record_purchase(book_id, branch_id)

            return jsonify({"message": "Book purchase successful"}), 200
        else:
            return jsonify({"message": "The book is out of stock in this branch"}), 400
    else:
        return jsonify({"message": "The book is not available"}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5001)
