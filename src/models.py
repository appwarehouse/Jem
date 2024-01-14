
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Announcement(Base):
    __tablename__ = 'announcements'

    id = Column(Integer, primary_key=True)
    run_status = Column(String, default='scheduled')
    scheduled_time = Column(DateTime)
    announcement_message = Column(String)
    client_id = Column(Integer)

    def __repr__(self):
        return f"<Announcement(id={self.id}, run_status={self.run_status}, scheduled_time={self.scheduled_time}, " \
               f"announcement_message={self.announcement_message}, client_id={self.client_id})>"
    

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    surname = Column(String(255))
    phoneNumber = Column(String(20))
    client_id = Column(Integer)

    def __repr__(self):
        return f"<Contact(id={self.id}, name={self.name}, surname={self.surname}, phoneNumber={self.phoneNumber}, client_id={self.client_id})>"

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    announcement_id = Column(Integer)
    message = Column(String)
    recipient_number = Column(String)
    status = Column(String, default='created')
    status_timestamp = Column(DateTime, default=datetime.utcnow)
    error_message = Column(String)
    retries = Column(Integer, default=0)
    sent = Column(Boolean, default=False)