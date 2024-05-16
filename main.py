from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
  {
    "id":1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Fiction",
    "year_published": 1925,
    "ISBN": "9780743273565",
    "publisher": "Scribner"
  },
  {
    "id":2,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Fiction",
    "year_published": 1960,
    "ISBN": "9780061120084",
    "publisher": "Harper Perennial Modern Classics"
  },
  {
    "id":3,
    "title": "1984",
    "author": "George Orwell",
    "genre": "Dystopian Fiction",
    "year_published": 1949,
    "ISBN": "9780451524935",
    "publisher": "Signet Classic"
  },
  {
    "id":4,
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "genre": "Fiction",
    "year_published": 1951,
    "ISBN": "9780316769488",
    "publisher": "Little, Brown and Company"
  },
  {
    "id":5,
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "genre": "Romance",
    "year_published": 1813,
    "ISBN": "9780141439518",
    "publisher": "Penguin Classics"
  }
]

# This will show our Greeting page.
@app.route('/Home',methods = ['GET'])
def home_page():
    return "Hello."



# This will show all our books data.
@app.route('/Home/books',methods = ['GET'])
def book_data():
    return jsonify(books)


# This will show a single book data.
@app.route('/Home/books/<int:book_id>',methods=['GET'])
def single_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'message':'Book not Found.'})


# This will add a new book.
@app.route('/Home/add_book',methods = ['POST'])
def add_book():
    new_book = {
        "id" : request.json['id'],
        "title" : request.json['author'],
        "author" : request.json['author'],
        "genre" : request.json['genre'],
        "year_published" : request.json['year_published'],
        "ISBN" : request.json['ISBN'],
        "publisher" : request.json['publisher']
    }
    books.append(new_book)
    return jsonify({'message': 'Book added succesfully.'})



   
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=4500)