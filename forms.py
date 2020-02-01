from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, BooleanField
from wtforms.validators import DataRequired

class TextBox(FlaskForm):
    text = TextAreaField('Enter an Abstract', validators=[DataRequired()])
    submit = SubmitField('Match')

class MatchForm(FlaskForm):
    relevance = BooleanField('Is the abstract relevant?')
    cancer = StringField('Name of Cancer')
    drug = StringField("Name of Drug")
    submit = SubmitField('Submit')