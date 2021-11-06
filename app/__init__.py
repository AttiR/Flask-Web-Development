from flask import Flask

app = Flask(__name__)

from app import views # import views from app package
from app import admin_views
