from flask import Flask
import wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email

class RegisterForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired(), Length(min=8, max=15)])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired(), Length(min=8, max=15)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')

