import datetime as dt
from flask import make_response, jsonify, render_template, session
from flask_restful import Resource, reqparse
from models.schedule_email import ScheduledEmail
from modules.helper import non_empty_string, extract_arguments
from models.event import Event
from models.attendees import Attendees
from models.event_attendees import EventAttendees


class PostCreateEvent(Resource):
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('event_name', type=non_empty_string, location='form',
                            nullable=False, help='Error, field event_name is empty')
        parser.add_argument('event_description', type=non_empty_string, location='form',
                            nullable=False, help='Error, field event_name is empty')
        parser.add_argument('attendee_name', type=non_empty_string, location='form', action='append',
                            nullable=False, help='Error, field event_name is empty')
        parser.add_argument('attendee_email', type=non_empty_string, location='form', action='append',
                            nullable=False, help='Error, field event_name is empty')

        args = parser.parse_args()
        event_name, event_description, attendee_name, attendee_email = extract_arguments(args)

        # add to table Event
        event = Event(event_name=event_name, event_description=event_description)
        event_id = event.save_to_db()

        # add to table Attendees
        attendee_ids = []
        if event_id:
            if len(attendee_name) != len(attendee_email):
                return make_response(jsonify({"message": "attendee_name and attendee_email missmatch"}), 400)
            for data in zip(attendee_name, attendee_email):
                attendee = Attendees(attendee_name=data[0], attendee_email=data[1])
                attendee_id = attendee.save_to_db()
                if not attendee_id:
                    # attendee_id already exist, get id instead
                    _result = attendee.find_by_attendee_name(data[0])
                    attendee_id = _result.id
                attendee_ids.append(attendee_id)

        # add to table EventAttendees
        for _attendee_id in attendee_ids:
            event_attendee = EventAttendees(attendees_id=_attendee_id, event_id=event_id)
            event_attendee.save_to_db()

        return make_response(jsonify({"event_id": event_id}), 200)


class GetManageEvent(Resource):
    def __init__(self):
        pass

    def get(self, event_id=0):
        event = Event()
        result = event.find_by_event_id(event_id)
        session['event_id'] = event_id

        schedule_email = ScheduledEmail()
        all_schedules = []
        for sch in schedule_email.find_by_event_id(event_id):
            all_schedules.append({
                'id': sch.id,
                'subject': sch.subject,
                'content': sch.content,
                'timestamp': sch.timestamp.strftime("%Y-%m-%dT%H:%S:%M")
            })

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('manage_event.html',
                                             event_name=result.event_name,
                                             event_description=result.event_description,
                                             schedules=all_schedules,
                                             event_id=event_id), 200, headers)
