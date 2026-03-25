from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired("This is a required field"), Email() ])
    password = PasswordField(label='Password')
    submit = SubmitField(label='Log In')

