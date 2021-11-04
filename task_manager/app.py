# A simple to do app to cick off with databse and forms in Flask

from re import template
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
load_dotenv()
import os


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = os.getenv('MY_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # we dont want to track modifications in database

db = SQLAlchemy(app) # it will connect the databse with app

# model defines how datastructure look likes
class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task_text = db.Column(db.String(150), index =True) 


tasks = []

# form to ask user for input

class taskForm(FlaskForm):
    task = StringField("Task", validators=[DataRequired(),  Length(min=5, max=100)]) #"Task is label"
    submit = SubmitField("Add Task")

# how to initialize the database
db.create_all()       

@app.route("/", methods = ["GET", "POST"])
def index():
    # some logic so that our router handle the post request
    template_form = taskForm()
    
    if 'task' in request.form:
            #tasks.append(request.form['task'])
            db.session.add(Task(task_text = request.form['task'])) # now we are adding in database
            db.session.commit()

    return render_template("index.html", tasks = Task.query.all(), template_form = template_form) # we need pass newinstance object of class form