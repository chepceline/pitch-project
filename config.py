import os
class Config:
    
    SECRET_KEY ='aa;ag8CFuGqen;YpA}}-G%64C}ggiN'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT =587
    MAIL_USE_TLS =True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')


class ProdConfig(Config):
    

    pass

class DevConfig(Config):
    DEBUG = True
    

config_options= {
    'development':DevConfig,
    'production':ProdConfig
}