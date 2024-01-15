from fastapi import Depends, FastAPI
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import declarative_base, Session
from models import Announcement
from db import get_db
from typing import Optional

app = FastAPI()
Base = declarative_base()


class AnnouncementBase(BaseModel):
    run_status: str
    scheduled_time: datetime
    announcement_message: str
    client_id: int

@app.post("/announcements")
def create_announcement(announcement: AnnouncementBase, db: Session = Depends(get_db)):
    db_announcement = Announcement(**announcement.dict())
    db.add(db_announcement)
    db.commit()
    db.refresh(db_announcement)
    return db_announcement

@app.get("/")
def index():
    return {
        "success": True,
        "message": "Leggo"
    }