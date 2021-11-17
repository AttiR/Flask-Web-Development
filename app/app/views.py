

from app import app # so that its run as it is in root
from flask import render_template, request, url_for, redirect


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
    
@app.route("/sign-up")
def register():
    
    return render_template("public/signup.html")

@app.route("/login")
def login():
   
    return render_template("public/login.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():

    if request.method == "POST":
        req= request.form # return as disctionary
        name = req['name'] # req.get('name) # request.form['name']
        print(name)
        return redirect(request.url)
    
    return render_template("public/contact.html")    

data = {
     "Atti": {

    "name": "Atti",
    "profession": "engineer"}

}

@app.route("/profile/<username>")
def prof(username):

    user = None
    if username in data:
        user = data[username]
    return render_template("public/profile.html", user=user)

# Json data
@app.route("/json", methods=['POST', 'GET'])  
def json():
    return 'Thanks', 200