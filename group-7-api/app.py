from flask import Flask, jsonify, request
from db_utils import get_authors_records

app = Flask(__name__)
@app.route('/authors')
def get_authors():
    result = get_authors_records()
    return jsonify(result)

@app.route('/books', methods=['GET'])
def get_books():
    books = db_utils.get_all_books()
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

if __name__ == '__main__':
    app.run(debug=True, port=5001)
