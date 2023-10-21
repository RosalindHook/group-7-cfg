from flask import Flask, jsonify, request
from db_utils import get_authors_records

app = Flask(__name__)
@app.route('/authors')
def get_authors():
    result = get_authors_records()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)