from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, URL

class MovieForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    year = IntegerField(label='Year', validators=[DataRequired()])
    description = TextAreaField(label='Description', validators=[DataRequired()])
    rating = FloatField(label='Rating', validators=[DataRequired()])
    ranking = IntegerField(label='Ranking', validators=[DataRequired()])
    review = TextAreaField(label='Review', validators=[DataRequired()])
    img_url = StringField(label='Image URL', validators=[DataRequired(), URL()])
    submit = SubmitField(label='Add')