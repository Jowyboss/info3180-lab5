# Add any form classes for Flask-WTF here

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[InputRequired(), Length(max=100)])
    description = TextAreaField('Movie Description', validators=[InputRequired(), Length(max=600)])
    poster = FileField('Movie Poster', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Only .png, .jpeg, and .jpg files allowed')])