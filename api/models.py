from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    editorial_id = db.Column(db.Integer, db.ForeignKey('editorial.id'), nullable=False)
    releasedate = db.Column(db.String(120), unique=False, nullable=True)

    genre = db.relationship('Genres', back_populates='books')
    author = db.relationship('Authors', back_populates='books')
    editorial = db.relationship('Editorial', back_populates='books')

    def __repr__(self):
        return f'<Books {self.name}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "genre": self.genre.name if self.genre else None,
            "author": self.author.name if self.author else None,
            "editorial": self.editorial.name if self.editorial else None,
            "releasedate": self.releasedate,
        }
    
class Authors(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    books = db.relationship('Books', back_populates='author')

    def __repr__(self):
        return f'<Authors {self.name}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "books": [books.serialize() for books in self.books],
        }
    
class Genres(db.Model):
    __tablename__ = "genres"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    books = db.relationship('Books', back_populates='genre')

    def __repr__(self):
        return f'<Genres {self.name}>'
    
    def serialize(self):
        return {
            "id": self.id,  
            "name": self.name,
            "books": [books.serialize() for books in self.books],
        }
    
class Editorial(db.Model):
    __tablename__ = "editorial"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False) 

    books = db.relationship('Books', back_populates='editorial')

    def __repr__(self):
        return f'<Editorial {self.name}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "books": [books.serialize() for books in self.books],
        }