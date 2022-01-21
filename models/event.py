from modules.extensions import db
from sqlalchemy.exc import IntegrityError


class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(255), unique=True)
    event_description = db.Column(db.String(1024))

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.flush()
        except IntegrityError:
            # duplicate unique key
            db.session.rollback()
            print("Error insert: duplicate unique key in table Event")
            return None
        finally:
            db.session.commit()
            return self.id

    @classmethod
    def delete_by_event_id(cls, event_id):
        try:
            cls.query.filter_by(id=event_id).delete()
            db.session.flush()
        except Exception as err:
            # something error
            print(err)
            db.session.rollback()
            return False
        finally:
            db.session.commit()
        return True

    @classmethod
    def find_by_event_name(cls, event_name):
        return cls.query.filter_by(event_name=event_name).first()
