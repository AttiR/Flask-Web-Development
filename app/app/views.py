from flask.templating import render_template
from app import app # so that its run as it is in root
from flask import render_template

@app.route("/")
def index():
    return  render_template("public/index.html")

@app.route("/about")   
def about():
     return render_template("public/about.html")
