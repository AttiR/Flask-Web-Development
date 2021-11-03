from flask import Flask, render_template, request, url_for, flash, redirect
from forms import RegisterForm, LoginForm, FeedbackForm
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("MY_KEY")


bootstrap = Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html")

# routes for forms
@app.route("/register")
def register():
    form = RegisterForm()
    return render_template("signup.html", title = 'Register', form= form)

@app.route("/login")
def login():
    form= LoginForm()
    return render_template("login.html", title = 'Login', form= form)

@app.route("/contact")
def contact():
    form= FeedbackForm()
    return render_template("contact.html", title = 'contact', form= form)



