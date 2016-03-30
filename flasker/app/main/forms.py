from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PostForm(Form):
    body = TextAreaField("what's on your mind?", validators=[DataRequired()])
    submit = SubmitField('Submit')