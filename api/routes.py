from flask import Blueprint, request, jsonify
from flask_cors import CORS
from api.models import db, Books, Authors, Genres, Editorial

api = Blueprint('api', __name__)
CORS(api) 


@api.route('/books', methods=['GET', 'POST'])
def handle_books():
    response_body = {}
    
    if request.method == 'GET':
        rows = db.session.execute(db.select(Books)).scalars()
        results = [row.serialize() for row in rows]
        response_body['results'] = results
        response_body['message'] = "GET received"
        return response_body, 200
        
    if request.method == 'POST':
        data = request.json
        name = data.get('name')
        genre = data.get('genre') 
        author = data.get('author') 
        editorial = data.get('editorial') 
        releasedate = data.get('releasedate')

        if not all([name, genre, author, editorial, releasedate]):
            response_body['message'] = 'Missing data'
            return response_body, 400

        genre = Genres.query.filter_by(name=genre).first()
        author = Authors.query.filter_by(name=author).first()
        editorial = Editorial.query.filter_by(name=editorial).first()

        if not all([genre, author, editorial]):
            response_body['message'] = 'One or more entries not found'
            return response_body, 404

        new_book = Books(
            name=name, 
            genre=genre,
            author=author,
            editorial=editorial,
            releasedate=releasedate
        )
        
        db.session.add(new_book)
        db.session.commit()
        response_body['message'] = "Book created"
        return response_body, 201 
    

@api.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_books_id(id):
    response_body = {}
    
    if request.method == 'GET':
        row = Books.query.get(id)
        if row is None:
            response_body['message'] = 'Book not found'
            return response_body, 404
        response_body['results'] = row.serialize()
        response_body['message'] = "GET received"
        return response_body, 200
    
    if request.method == 'PUT':
        data = request.json
        name = data.get('name')
        genre = data.get('genre') 
        author = data.get('author') 
        editorial = data.get('editorial') 
        releasedate = data.get('releasedate')

        if not all([name, genre, author, editorial, releasedate]):
            response_body['message'] = 'Missing data'
            return response_body, 400
        row = Books.query.get(id)
        if row is None:
            response_body['message'] = 'Book not found'
            return response_body, 404

        genre = Genres.query.filter_by(name=genre).first()
        author = Authors.query.filter_by(name=author).first()
        editorial = Editorial.query.filter_by(name=editorial).first()

        if not all([genre, author, editorial]):
            response_body['message'] = 'One or more entries not found'
            return response_body, 404
        
        row.name = name
        row.genre_id = genreid
        row.author_id = author.id
        row.editorial_id = editorial.id
        row.releasedate = releasedate
        db.session.commit()
        response_body['message'] = "Book updated"
        return response_body, 200

    if request.method == 'DELETE':
        row = Books.query.get(id)
        if row is None:
            response_body['message'] = 'Book not found'
            return response_body, 404
        db.session.delete(row)
        db.session.commit()
        response_body['message'] = "Book deleted"
        return response_body, 200


@api.route('/authors', methods=['GET', 'POST'])
def handle_authors():
    response_body = {}
    if request.method == 'GET':
        rows = db.session.execute(db.select(Authors)).scalars()
        results = [row.serialize() for row in rows]
        response_body['results'] = results
        response_body['message'] = "GET received"
        return response_body, 200
    
    if request.method == 'POST':
        data = request.json
        name = data.get('name')
        if not name:
            response_body['message'] = 'Missing data'
            return response_body, 400
        new_author = Authors(name=name)
        db.session.add(new_author)
        db.session.commit()
        response_body['message'] = "Author created"
        return response_body, 201

@api.route('/authors/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_authors_id(id):
    response_body = {}
    if request.method == 'GET':
        row = Authors.query.get(id)
        if row is None:
            response_body['message'] = 'Author not found'
            return response_body, 404
        response_body['results'] = row.serialize()
        response_body['message'] = "GET received"
        return response_body, 200
    
    if request.method == 'PUT':
        data = request.json
        name = data.get('name')
        if not name:
            response_body['message'] = 'Missing data'
            return response_body, 400
        row = Authors.query.get(id)
        if row is None:
            response_body['message'] = 'Author not found'
            return response_body, 404
        row.name = name
        db.session.commit()
        response_body['message'] = "Author updated"
        return response_body, 200
    
    if request.method == 'DELETE':
        row = Authors.query.get(id)
        if row is None:
            response_body['message'] = 'Author not found'
            return response_body, 404
        db.session.delete(row)
        db.session.commit()
        response_body['message'] = "Author deleted"
        return response_body, 200

# Genres Routes
@api.route('/genres', methods=['GET', 'POST'])
def handle_genres():
    response_body = {}
    if request.method == 'GET':
        rows = db.session.execute(db.select(Genres)).scalars()
        results = [row.serialize() for row in rows]
        response_body['results'] = results
        response_body['message'] = "GET received"
        return response_body, 200

    if request.method == 'POST':
        data = request.json
        name = data.get('name')
        if not name:
            response_body['message'] = 'Missing data'
            return response_body, 400
        new_genre = Genres(name=name)
        db.session.add(new_genre)
        db.session.commit()
        response_body['message'] = "Genre created"
        return response_body, 201

@api.route('/genres/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_genres_id(id):
    response_body = {}
    if request.method == 'GET':
        row = Genres.query.get(id)
        if row is None:
            response_body['message'] = 'Genre not found'
            return response_body, 404
        response_body['results'] = row.serialize()
        response_body['message'] = "GET received"
        return response_body, 200
    
    if request.method == 'PUT':
        data = request.json
        name = data.get('name')
        if not name:
            response_body['message'] = 'Missing data'
            return response_body, 400
        row = Genres.query.get(id)
        if row is None:
            response_body['message'] = 'Genre not found'
            return response_body, 404
        row.name = name
        db.session.commit()
        response_body['message'] = "Genre updated"
        return response_body, 200
    
    if request.method == 'DELETE':
        row = Genres.query.get(id)
        if row is None:
            response_body['message'] = 'Genre not found'
            return response_body, 404
        db.session.delete(row)
        db.session.commit()
        response_body['message'] = "Genre deleted"
        return response_body, 200

# Editorial Routes
@api.route('/editorial', methods=['GET', 'POST'])
def handle_editorial():
    response_body = {}
    if request.method == 'GET':
        rows = db.session.execute(db.select(Editorial)).scalars()
        results = [row.serialize() for row in rows]
        response_body['results'] = results
        response_body['message'] = "GET received"
        return response_body, 200
    
    if request.method == 'POST':
        data = request.json
        name = data.get('name')
        if not name:
            response_body['message'] = 'Missing data'
            return response_body, 400
        new_editorial = Editorial(name=name)
        db.session.add(new_editorial)
        db.session.commit()
        response_body['message'] = "Editorial created"
        return response_body, 201

@api.route('/editorial/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_editorial_id(id):
    response_body = {}
    if request.method == 'GET':
        row = Editorial.query.get(id)
        if row is None:
            response_body['message'] = 'Editorial not found'
            return response_body, 404
        response_body['results'] = row.serialize()
        response_body['message'] = "GET received"
        return response_body, 200
    
    if request.method == 'PUT':
        data = request.json
        name = data.get('name')
        if not name:
            response_body['message'] = 'Missing data'
            return response_body, 400
        row = Editorial.query.get(id)
        if row is None:
            response_body['message'] = 'Editorial not found'
            return response_body, 404
        row.name = name
        db.session.commit()
        response_body['message'] = "Editorial updated"
        return response_body, 200
    
    if request.method == 'DELETE':
        row = Editorial.query.get(id)
        if row is None:
            response_body['message'] = 'Editorial not found'
            return response_body, 404
        db.session.delete(row)
        db.session.commit()
        response_body['message'] = "Editorial deleted"
        return response_body, 200
