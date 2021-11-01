from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_bootstrap import Bootstrap, bootstrap_find_resource



app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = "my_secret_key"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

todos = ['flask_setup', 'write_code', 'run_code']
@app.route("/")
def index():
    return render_template("index.html", todos = todos)


# dynamic routes
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)