from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from modules.helper import non_empty_string, extract_arguments
from models.schedule_email import ScheduledEmail
from modules.extensions import celery


class PostSaveEmails(Resource):
    """To be used by Flask.add_resource."""
    def __int__(self, **kwargs):
        self.app = kwargs['app']

    def post(self):
        """Handle method post of endpoint /save_emails
        :return: "Response"
        """
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('event_id', type=int, required=True, location='form',
                            nullable=False, help='Error, field event_id is empty')
        parser.add_argument('email_subject', type=non_empty_string, required=True, location='form',
                            nullable=False, help='Error, field email_subject is empty')
        parser.add_argument('email_content', type=non_empty_string, required=True, location='form',
                            nullable=False, help='Error, field email_content is empty')
        parser.add_argument('timestamp', type=non_empty_string, required=True, location='form',
                            nullable=False, help='Error, field timestamp is empty')
        args = parser.parse_args()
        event_id, email_subject, email_content, timestamp = extract_arguments(args)

        schedule_email = ScheduledEmail(subject=email_subject,
                                        content=email_content,
                                        timestamp=timestamp,
                                        event_id=event_id)
        schedule_email.save_to_db()

        # TODO: get recipients, attendees email's of this current event_id
        send_email(self.app, )


        return make_response(jsonify({"message": "OK"}), 200)
