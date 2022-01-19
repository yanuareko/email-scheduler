import logging
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from modules.helper import non_empty_string, extract_arguments


class PostSaveEmails(Resource):
    """To be used by add_resource"""
    def __init__(self, **kwargs):
        self.value: str = "sample value"
        self.logger: logging.getLogger = kwargs["logger"]
        self.db: SQLAlchemy = kwargs["db"]

    def post(self):
        """Handle method post of endpoint /save_emails
        :return: "Response"
        """
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('event_id', type=int, required=True, nullable=False)
        parser.add_argument('email_subject', type=non_empty_string, required=True, nullable=False)
        parser.add_argument('email_content', type=non_empty_string, required=True, nullable=False)
        parser.add_argument('timestamp', type=non_empty_string, required=True, nullable=False)
        args = parser.parse_args()
        event_id, email_subject, email_content, timestamp = extract_arguments(args)

        self.logger.info("save-emails -- event_id=%s" % event_id)
        return make_response(jsonify({"msg": self.value}), 200)
