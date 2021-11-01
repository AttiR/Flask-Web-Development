# A simple to do app to cick off with databse and forms in Flask

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

# for practice lets save data locally
tasks = ['vscode_setup', 'flask_setup', 'happy_coding']

# form to ask user for input

class taskForm(FlaskForm):
    task = StringField("Task") #label
    submit = SubmitField("Add Task")

@app.route("/", methods = ["GET", "POST"])
def index():
    # some logic so that our router handle the post request
    if 'task' in request.form:
        tasks.append(request.form['task'])

    return render_template("index.html", tasks = tasks, template_form = taskForm()) # we need pass newinstance object of class form