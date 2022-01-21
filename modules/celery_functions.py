from flask_mail import Message
from modules.extensions import celery, mail


@celery.task()
def send_email_asynchronous(email_subject, email_content, email_recipients):
    """Background task to send an email with Flask-Mail."""
    msg = Message(email_subject, recipients=email_recipients)
    msg.body = email_content
    # with app.app_context():
    mail.send(msg)
