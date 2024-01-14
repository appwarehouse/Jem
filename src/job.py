# job.py

from celery import Celery
from schedule_announcements import create_messages_for_announcement
from datetime import datetime, timedelta
from models import Announcement
from models import Message
from db import get_db

celery = Celery('job', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0', include=['tasks'])

@celery.task(name='job.process_scheduled_jobs')
def process_scheduled_jobs():
    try:
        session = get_db()

        current_time = datetime.utcnow()
        scheduled_announcements = session.query(Announcement).filter(
            Announcement.run_status == 'scheduled',
            Announcement.scheduled_time <= current_time
        ).all()

        for announcement in scheduled_announcements:
            try:            
                announcement.run_status = 'running'
                session.commit()

                create_messages_for_announcement.delay(announcement.id, session)

                announcement.run_status = 'run'
                session.commit()
            except Exception as te:
                print(f"Error processing scheduled jobs: {te}")
            finally:
                if announcement.run_status == 'running':
                    announcement.run_status = 'error'
                    session.commit()
    
    except Exception as e:
        # Handle exceptions (log, print, etc.)
        print(f"Error processing scheduled jobs: {e}")
    finally:
        if session:
            session.close()

celery.conf.beat_schedule = {
    'process-announcements-every-5-minutes': {
        'task': 'tasks.process_announcements',
        'schedule': timedelta(minutes=5),
    },
}
