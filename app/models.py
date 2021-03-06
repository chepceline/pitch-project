from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),index = True)
    email= db.Column(db.String(255),unique = True, index = True)
    password_secure= db.Column(db.String(255))
    pitches=db.relationship('Pitches',backref='user',lazy='dynamic')
    profile_pic_path= db.Column(db.String())
    
    
    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

class Pitches(db.Model):
    __tablename__='pitches'
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(250))
    description=db.Column(db.String(250))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    



class Coments(db.Model):
    __tablename__='coments'
    id=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(250))
    comment= db.Column(db.String())
    # users=db.relationship('User',backref='role',lazy='dynamic')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


