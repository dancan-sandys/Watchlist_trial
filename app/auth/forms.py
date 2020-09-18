from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import Required,Email, EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):

    email = StringField('Your email address', validators=[Required(), Email()])
    username = StringField('Enter your username', validators= [Required()])
    password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message='passwords must match')])
    password_confirm = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Sign up')

    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an existing account with that username')

    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('There is an existing account with that username')

class LoginForm(FlaskForm):
    email= StringField('Your email address', validators=[Required(), Email()])
    password = PasswordField('Your password', validators=[Required(),])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')