from modules.extensions import db
from sqlalchemy.exc import IntegrityError


class Attendees(db.Model):
    __tablename__ = 'attendees'
    id = db.Column(db.Integer, primary_key=True)
    attendee_name = db.Column(db.String(255), unique=True)
    attendee_email = db.Column(db.String(128), unique=True)

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.flush()
        except IntegrityError:
            # duplicate unique key
            db.session.rollback()
            print("Error insert: duplicate unique key in table Attendees")
            return None
        finally:
            db.session.commit()
            return self.id

    @classmethod
    def find_by_attendee_name(cls, attendee_name):
        return cls.query.filter_by(attendee_name=attendee_name).first()

    @classmethod
    def find_by_attendee_email(cls, attendee_email):
        return cls.query.filter_by(attendee_email=attendee_email).first()
