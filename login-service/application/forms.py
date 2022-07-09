from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email_address = StringField(label='email')
    password1 = PasswordField(label='password1')
    password2 = PasswordField(label='password2')
    submit = SubmitField(label='submit')
