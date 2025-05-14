from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base


class Message(Base):
    __tablename__ = 'MESSAGES'

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.student_id'), nullable=False)
    subject = Column(String(100), nullable=True)
    body = Column(String(250), nullable=False)
    sent_at = Column(DateTime)
    direction = Column(String(25)) # email, 'manual', etc
    # These are set by the trigger
    created_date = Column(DateTime, default=datetime.now())
    modified_date = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    student = relationship("Student", back_populates="messages")