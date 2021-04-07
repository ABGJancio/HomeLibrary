from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    id = IntegerField('id')
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    genre = StringField('genre', validators=[DataRequired()])
    release_year = IntegerField('release_year', validators=[DataRequired()])
    series = StringField('series')
    read = BooleanField('read')
    review = TextAreaField('review')
