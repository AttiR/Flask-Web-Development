from flask import Flask, request, flash, redirect, url_for

from flask.templating import render_template
from flask_mail import Mail, Message
from form import FeedbackForm
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)
mail= Mail(app)
app.config['SECRET_KEY'] = os.getenv("MY_KEY")

    
bootstrap = Bootstrap(app)
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