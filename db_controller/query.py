from models.attendees import Attendees
from models.event import Event
from models.event_attendees import EventAttendees
from modules.extensions import db


def get_recipients(event_id) -> list:
    results = db.session.query(Attendees, EventAttendees, Event). \
        join(EventAttendees, EventAttendees.attendees_id == Attendees.id). \
        join(Event, Event.id == EventAttendees.event_id). \
        filter(Event.id == event_id). \
        order_by(Attendees.attendee_email).all()
    return results


def get_recipients_emails(event_id) -> list:
    results = get_recipients(event_id)
    return [recipient.attendee_email for recipient, _, _ in results]


def get_recipients_emails_n_name(event_id) -> list:
    results = get_recipients(event_id)
    return [(recipient.attendee_name, recipient.attendee_email)for recipient, _, _ in results]
