import datetime as dt

import pytz
from flask_restful import Resource, reqparse
from flask import jsonify, make_response, render_template, session, request

from models.event import Event
from modules.form_email_schedule import EmailForm
from modules.helper import non_empty_string, extract_arguments, wanted_time_format
from models.schedule_email import ScheduledEmail
from db_controller.query import get_recipients
from modules.celery_functions import send_email_asynchronous


class PostSaveEmails(Resource):
    """To be used by Flask.add_resource."""
    def __init__(self, **kwargs):
        self.app = kwargs['app']

    def get(self):
        event = Event()
        event_id = session.get('event_id', None)
        result = event.find_by_event_id(event_id)

        form = EmailForm(event_id=event_id)
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('form_email.html', title=result.event_name, form=form), 200, headers)

    def post(self):
        """Handle method post of endpoint /save_emails
        :return: "Response"
        """
        parser = reqparse.RequestParser(bundle_errors=True)
        # parser.add_argument('event_id', type=int, required=True, location='form',
        #                     nullable=False, help='Error, field event_id is empty')
        parser.add_argument('subject', type=non_empty_string, required=True, location='form',
                            nullable=False, help='Error, field email_subject is empty')
        parser.add_argument('content', type=non_empty_string, required=True, location='form',
                            nullable=False, help='Error, field email_content is empty')
        parser.add_argument('timestamp', type=wanted_time_format, required=True, location='form',
                            nullable=False, help='Error, field timestamp is empty or unmatch format, '
                                                 'example: 2006-01-02T15:04')
        # email_subject = request.form.get('email_subject')
        # email_content = request.form.get('email_content')
        # timestamp = request.form.get('timestamp')
        event_id = request.form.get('event_id')
        if not event_id:
            event_id = session.get('event_id', None)

        args = parser.parse_args()
        email_subject, email_content, timestamp = extract_arguments(args)

        # convert string of timestamp to datetime
        local_tz = pytz.timezone(self.app.config['timezone'])
        dt_timestamp = local_tz.localize(dt.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M"))
        scheduled_email = ScheduledEmail(subject=email_subject,
                                         content=email_content,
                                         timestamp=dt_timestamp,
                                         event_id=event_id)
        scheduled_email.save_to_db()

        email_recipients = get_recipients(event_id)
        if not email_recipients:
            return make_response(jsonify({"message": "Error, this event doesn't have attendees"}), 400)

        # celery asynchronous worker
        send_email_asynchronous.apply_async(
            kwargs={"email_subject": email_subject,
                    "email_content": email_content,
                    "email_recipients": email_recipients},
            eta=dt_timestamp
        )

        return make_response(jsonify({"message": "OK"}), 200)
