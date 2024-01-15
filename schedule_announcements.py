from celery import Celery
from models import Message, Contact, Announcement
from tasks import process_announcements

celery = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0', include=['tasks'])

@celery.task(name='tasks.create_messages_for_announcement')
def create_messages_for_announcement(announcement_id, session):
    try:
        announcement = session.query(Announcement).get(announcement_id)
        client_id = announcement.client_id

        recipient_numbers = session.query(Contact.recipient_number).filter(Contact.client_id == client_id).all()

        for recipient_number in recipient_numbers:
            message = Message(announcement_id=announcement.id, message=announcement.announcement_message, recipient_number=recipient_number)
            session.add(message)
            session.commit()

        process_announcements.apply_async(args=[announcement_id])

    except Exception as e:
        print(f"Error creating messages for announcement: {e}")

