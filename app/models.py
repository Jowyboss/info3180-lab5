# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import date

class Movie(db.Model):

    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    poster = db.Column(db.String(200))
    created_at = db.Column(db.DateTime)

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = date.today().strftime('%d-%m-%Y')

    
    def __repr__(self):
        return f'Movie {self.title, self.description, self.created_at}'