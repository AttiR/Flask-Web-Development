from flask.templating import render_template
from app import app # so that its run as it is in root
from flask import render_template

@app.route("/")
def index():

    return  render_template("public/index.html")

@app.route("/about")   
def about():
     return render_template("public/about.html")
@app.route("/jinja")  
def jinja():
    name = "Ali"
    age = 30

    class Car:
        def __init__(self, name, color, brand):
            self.color= color
            self.brand= brand
            self.name = name

        def features(self):
            return f'The colour of {self.name} is, {self.color} and brand is {self.brand}'   

    car = Car('Honda', 'Black', 'Civic')  
    info = car.features()  

    fruits = ['apple', 'bnana', 'mango']

    my_html= "<h1>hello</h1>"
    return render_template("public/jinja.html", name=name, fruits=fruits, age=age, info=info, my_html=my_html)   
