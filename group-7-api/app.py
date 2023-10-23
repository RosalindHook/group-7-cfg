from flask import Flask, jsonify, request
from db_utils import get_authors_records, get_all_books, get_random_books, check_book_availability, get_book_stock_info, \
    update_book_stock, insert_donated_book

app = Flask(__name__)
@app.route('/authors')
def get_authors():
    result = get_authors_records()
    return jsonify(result)


@app.route('/books', methods=['GET'])
def get_books():
    books = get_all_books()
    if books:
        # convert tuples to dictionary list for JSON formatting
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
    availability_result, stock = check_book_availability(book_id, branch_id)

    if availability_result:
        if stock > 0:
            # Update the stock in your database (decrease stock count by 1)
            update_book_stock(book_id, branch_id, stock - 1)

            return jsonify({"message": "Book purchase successful"}), 200
        else:
            return jsonify({"message": "The book is out of stock in this branch"}), 400
    else:
        return jsonify({"message": "The book is not available"}), 400


@app.route('/stock', methods=['GET'])
def get_stock_info():
    stock_info = get_book_stock_info()  # returns all stock info

    if stock_info:
        # convert tuples to dictionary list for JSON formatting
        formatted_stock_info = [
            {
                "BookID": book_id,
                "Book title": title,
                "Branch": branch,
                "Stock": stock
            }
            for book_id, title, branch, stock in stock_info
        ]
        return jsonify(formatted_stock_info)
    else:
        return jsonify([])  # return empty list if no books found



@app.route('/bonus')
def get_bonus():
    bonus = get_random_books(num_books=3)
    if bonus:
        books_data = [
            {
                "BookID": book_id,
                "Title": title,
                "Author": author,
                "Price": price
            }
            for book_id, title, author, price in bonus
        ]
        return jsonify(books_data)
    else:
        return jsonify([])  # if no books found, return empty list


@app.route('/donate', methods=['POST'])
def donate_book():
    data = request.get_json()

    # Extract book details from the JSON data
    title = data.get('title')
    author = data.get('author')
    genre = data.get('genre')
    condition = data.get('condition')
    description = data.get('description')

    # Insert the donated book into the database using the new function
    insert_donated_book(title, author, genre, condition, description)

    return jsonify({"message": "Book donation successful"})


if __name__ == '__main__':
    app.run(debug=True, port=5003)
