from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = "my_secret_key"

todos = ['flask_setup', 'write_code', 'run_code']
@app.route("/")
def index():
    return render_template("index.html", todos = todos)

# dynamic routes
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)