from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired


class EmailForm(FlaskForm):
    subject = StringField('Email Subject', validators=[DataRequired()])
    content = StringField('Email Content', widget=TextArea(), validators=[DataRequired()])
    timestamp = DateTimeLocalField('Time to Send', format='%d/%m/%Y %H:%M')
    # event_id = None
    submit = SubmitField('Submit')
