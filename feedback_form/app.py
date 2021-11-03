from flask import Flask, request, flash, redirect, url_for
from flask.templating import render_template
from form import FeedbackForm
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("MY_KEY")


bootstrap = Bootstrap(app)

@app.route("/", methods = ['GET', 'POST'])
def contact():
    form = FeedbackForm()
    if form.validate_on_submit():
        pass
    return render_template ("contact.html", title = 'Feedback', form= form)