from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = DATABASE_URL = "postgresql://jemUser:jemUser123@localhost:5432/jem_assessment_poc"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()