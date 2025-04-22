from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    direction = Column(String(255), nullable=True)
    body = Column(Text, nullable=False)
    status = Column(String(50), default='Pending') # 'delivered', 'failed', etc.
    source = Column(String(50), default='email') # email, 'manual', etc
    sent_at = Column(DateTime, default=datetime.now())

    # These are set by the trigger
    created_at = Column(DateTime)
    modified_at = Column(DateTime)

    student = relationship("Student", backref=("messages"))