import os
class Config:
    
    SECRET_KEY='aa;ag8CFuGqen;YpA}}-G%64C}ggiN'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT =587
    MAIL_USE_TLS =True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')


class ProdConfig(Config):
    
    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI = uri
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://damaris:1234@localhost/power'
    DEBUG = True
    

config_options= {
    'development':DevConfig,
    'production':ProdConfig
}