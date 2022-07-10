from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField(label='User Name', validators=length(min=5, max=20))
    email_address = StringField(label='Email Address')
    password1 = PasswordField(label='Password', validators=length(min=8))
    password2 = PasswordField(label='Confirm Password', validators=EqualTo('password1'))
    submit = SubmitField(label='Create Account')
