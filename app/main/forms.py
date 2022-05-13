from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired
from wtforms import ValidationError
from ..models import Pitches

class Pitch(FlaskForm):
  title = StringField('Enter the Title', validators=[DataRequired()])
  description= TextAreaField('Give brief description',validators=[DataRequired()])
  submit = SubmitField('Submit')


