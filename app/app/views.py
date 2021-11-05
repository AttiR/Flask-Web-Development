from app import app # so that its run as it is in root

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about")   
def about():
      return "<p> hello flask</p>"
