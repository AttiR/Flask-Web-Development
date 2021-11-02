from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("MY_KEY")

bootstrap = Bootstrap(app)

class Myform(FlaskForm):
    text = StringField('Name')
    submit = SubmitField('Submit')

    

@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html", template_form = Myform())