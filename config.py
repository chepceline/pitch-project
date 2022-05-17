import os
class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT =587
    MAIL_USE_TLS =True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI')

    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://celine:cel250@localhost/flask_db'
    SECRET_KEY ='aa;ag8CFuGqen;YpA}}-G%64C}ggiN'

config_options= {
    'development':DevConfig,
    'production':ProdConfig
}