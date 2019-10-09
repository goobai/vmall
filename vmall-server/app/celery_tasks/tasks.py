from app import mail, app
from flask_mail import Message
from .make_celery import make_celery

celery = make_celery(app)


@celery.task
def send_mail(subject, sender, recipients, body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = body
    with app.app_context():
        mail.send(msg)


@celery.task
def send_sms(phone):
    pass
