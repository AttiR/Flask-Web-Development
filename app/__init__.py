from flask import Flask, config

app = Flask(__name__)

if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')

elif app.config['ENV'] == 'development':
    app.config.from_object('config.DevelopmentConfig') 
else:
     app.config.from_object('config.TestingConfig')



from app import views # import views from app package
from app import admin_views
