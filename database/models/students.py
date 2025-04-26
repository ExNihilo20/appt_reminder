
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database.base import Base
from datetime import datetime

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email_address = Column(String(100), nullable=True)
    phone_number = Column(String(10), nullable=False)
    carrier = Column(String(25), nullable=False)
    enabled=Column(Boolean, default=True)
    
    # These are set by the trigger
    created_date = Column(DateTime, default=datetime.now())
    modified_date = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    messages = relationship("Message", back_populates="student")