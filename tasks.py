# tasks.py

from celery import Celery
from celery.utils.log import get_task_logger
from datetime import datetime
from sqlalchemy.orm import  declarative_base
from models import Announcement, Message
from db import get_db
import random


Base = declarative_base()

Session = get_db

celery = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0', include=['tasks'])

@celery.task(name='tasks.process_announcements')
def process_announcements(announcement_id = None):
    try:
        session = Session()

        if announcement_id :

            announcement = session.query(Announcement).filter(Announcement.id == announcement_id).first()

            if announcement.run_status != 'scheduled':
                return
            
            announcement.run_status = 'running'
            session.commit()

            messages = session.query(Message).filter(Message.announcement_id == announcement_id, Message.sent.is_(False)).all()

            for message in messages:
                status = 'sent' if send_message(message.recipient_number, message.message) else 'error'

                message.status = status
                message.status_timestamp = datetime.utcnow()

                if status == 'error':
                    message.retries += 1
                    message.error_message = 'Sending failed'

            announcement.run_status = 'run'
            session.commit()

    except Exception as e:
        {
            print(f"Error sending announcement: {e}")
        }
    finally:
        if session:
            session.close()

def send_message(recipient_number, message):
    
    result = random.choice([True, False])
    if result:
        print ("Sent message")
    else :
        print ("Message not sent")
    return result


