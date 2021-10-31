from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def show_books():
    books_bestseller = list(db.books.find({}, {'_id':False}))
    return jsonify({'books_bestsellers': books_bestseller})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
