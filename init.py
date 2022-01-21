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

