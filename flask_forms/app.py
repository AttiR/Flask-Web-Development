from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("MY_KEY")

bootstrap = Bootstrap(app)

class Myform(FlaskForm):
    text = StringField('Name', validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired(), Length(min=8, max=15)])
    submit = SubmitField('Submit')


    

@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html", template_form = Myform())