from flask import Flask, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask.templating import render_template
from flask_mail import Mail, Message
from form import FeedbackForm
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
load_dotenv()
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
mail= Mail(app)
admin=Admin(app)

app.config['SECRET_KEY'] = os.getenv("MY_KEY")
password = os.getenv('DATABASE_PASS')

# devlopment and production ENV Databse setup
ENV = 'dev'
if ENV == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/flask_feedback'
    app.debug= True
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    app.debug= False 
    


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# create database object
db = SQLAlchemy(app)

# Database Model
class Feedback(db.Model):
    __tablename__ = 'feedback'
    sno = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200))
    email= db.Column(db.String(200))
    feedback = db.Column(db.Text())

    # now we need to define the constructor
    def __init__(self, name, email, feedback):
        self.name=name
        self.email=email
        self.feedback=feedback




    

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'attirehman388@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv('PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

email_sent = False
@app.route("/", methods = ['GET', 'POST'])
def contact():
    form = FeedbackForm()
    if request.method == 'POST':
        req= request.form
        name = req['name']
        email = req['email']
        feedback = req['feedback']

        # databse entry
        data = Feedback(name, email, feedback)
        db.session.add(data)
        db.session.commit()
        
        # how to sent an email
        msg = Message('Feedback notification', sender = 'attirehman388@gmail.com', recipients = [email])
        msg.body = feedback
        mail.send(msg)
        email_sent = True
        if(email_sent):
            flash(f'Feedback has been sent, Thank you {name}!', 'success') # flash is an easy mthode to send one time alert
             # set the base layout for flash messages at base.html
            return redirect( url_for('contact') )
        else:
            return "email not sent"
        
    return render_template ("contact.html", title = 'Feedback', form= form)