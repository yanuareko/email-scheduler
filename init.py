from modules.config import load_config
from app import app
from modules.extensions import db

# Configurations
db_config: dict = load_config("./config.yml")["database"]
app.config["SQLALCHEMY_DATABASE_URI"]: str = db_config["uri"]

# Define the database object which is imported
# by modules and controllers

# Import models
from models.schedule_email import ScheduledEmail # noqa
from models.attendees import Attendees # noqa
from models.event import Event # noqa
from models.event_attendees import EventAttendees # noqa

# Build the tables:
with app.test_request_context():
    db.create_all()

    # add to table Event
    event = Event(event_name="Initial Event", event_description="Initial event description")
    event_id = event.save_to_db()

    # add to table Attendees
    attendee_ids = []
    if event_id:
        for data in zip(["user1", "user2"], ["yanuarem@gmail.com", "test.yanuareko@gmail.com"]):
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
