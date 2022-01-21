from modules.extensions import db

fk_scheduled_email_event = db.ForeignKey('event.id', ondelete='CASCADE', onupdate='CASCADE')
fk_event_attendees_event = db.ForeignKey('event.id', ondelete='CASCADE', onupdate='CASCADE')
fk_event_attendees_attendees = db.ForeignKey('attendees.id', ondelete='CASCADE', onupdate='CASCADE')
