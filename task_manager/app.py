# A simple to do app to cick off with databse and forms in Flask

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
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
    task = StringField("Task") #label
    submit = SubmitField("Add Task")

# how to initialize the database
db.create_all()       

@app.route("/", methods = ["GET", "POST"])
def index():
    # some logic so that our router handle the post request
    if 'task' in request.form:
        #tasks.append(request.form['task'])
        db.session.add(Task(task_text = request.form['task'])) # now we are adding in database
        db.session.commit()

    return render_template("index.html", tasks = Task.query.all(), template_form = taskForm()) # we need pass newinstance object of class form