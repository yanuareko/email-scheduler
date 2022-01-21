from modules.extensions import db
from models.foreign_keys import fk_scheduled_email_event


class ScheduledEmail(db.Model):
    __tablename__ = 'scheduled_email'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(128), unique=False)
    content = db.Column(db.String(1024), unique=False)
    timestamp = db.Column(db.DateTime)
    event_id = db.Column(db.Integer, fk_scheduled_email_event, nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.flush()
        db.session.commit()
        return self.id

    @classmethod
    def find_by_event_id(cls, event_id):
        return cls.query.filter_by(event_id=event_id)
