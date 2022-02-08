from email.generator import Generator
from database.mysql_engine import SessionLocal

def get_db()-> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        if db is not None:
            db.close()

