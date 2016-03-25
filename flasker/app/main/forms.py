from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class NameForm(Form):
    name = StringField('Your name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PostForm(Form):
    body = TextAreaField('Post', validators=[DataRequired()])
    submit = SubmitField('Submit')