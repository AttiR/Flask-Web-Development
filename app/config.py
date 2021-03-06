import os
from dotenv import load_dotenv

# load dotenv in the base root
# APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
# dotenv_path = os.path.join(APP_ROOT, '.env')
# load_dotenv(dotenv_path)

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    DEBUG=False
    TESTING=False

    SESSION_COOKIE_SECURE=True
    SECRET_KEY=os.getenv('SECRET_KEY')
    


class ProductionConfig(Config): 
    pass   

class DevelopmentConfig(Config):
    DEBUG=True

    SESSION_COOKIE_SECURE=False

class TestingConfig(Config): 
    TESTING= True  
    SESSION_COOKIE_SECURE=False 