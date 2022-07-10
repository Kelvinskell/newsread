from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='User Name', validators=[Length(min=5, max=20), DataRequired()])
    email_address = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')
