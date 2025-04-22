
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=False)
    carrier = Column(String(50), nullable=False)
    email = Column(String(100), nullable=True)
    enabled=Column(Boolean, default=True)

    # These are set by the trigger
    created_at = Column(DateTime)
    modified_at = Column(DateTime)