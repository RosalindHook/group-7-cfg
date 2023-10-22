from flask import Flask, jsonify #, request   placeholder as not yet used
from db_utils import get_authors_records, get_all_books,get_random_books

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




if __name__ == '__main__':
    app.run(debug=True, port=5003)
