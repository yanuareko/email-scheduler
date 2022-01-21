import email_validator
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Email


class EmailForm(FlaskForm):
    subject = StringField('Email Subject', validators=[DataRequired()])
    content = StringField('Email Content', widget=TextArea(), validators=[DataRequired()])
    timestamp = DateTimeLocalField('Time to Send', format='%d/%m/%Y %H:%M')
    event_id = HiddenField('Event ID')
    submit = SubmitField('Submit')


class EventForm(FlaskForm):
    event_name = StringField('Event Name', validators=[DataRequired()])
    event_description = StringField('Event Description', widget=TextArea(), validators=[DataRequired()])
    attendee_name = StringField('Attendee Name', validators=[DataRequired()])
    attendee_email = StringField('Attendee Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')
