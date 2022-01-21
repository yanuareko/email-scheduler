from modules.extensions import db
from models.foreign_keys import fk_event_attendees_event, fk_event_attendees_attendees


class EventAttendees(db.Model):
    __tablename__ = 'event_attendees'
    id = db.Column(db.Integer, primary_key=True)
    attendees_id = db.Column(db.Integer, fk_event_attendees_attendees, nullable=False)
    event_id = db.Column(db.Integer, fk_event_attendees_event, nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_attendees_id(cls, attendees_id):
        return cls.query.filter_by(attendees_id=attendees_id).first()

    @classmethod
    def find_by_event_id(cls, event_id):
        return cls.query.filter_by(event_id=event_id).first()
