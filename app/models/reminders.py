from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.base import Base


class Reminder(Base):
    __tablename__ = 'LU_REMINDER'
    reminder_id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(50), nullable=False)
    # These are set by the trigger
    created_date = Column(DateTime, default=datetime.now(), nullable=False)
    modified_date = Column(DateTime, default=datetime.now(), onupdate=datetime.now())