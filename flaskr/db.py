import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
from flask import current_app, g

from configparser import ConfigParser
import os

# CONFIGURATION MANAGEMENT
# ========================
def get_engine():
    if 'engine' not in g:

        # grab mysql strings
        parser = ConfigParser()

        # get the configuration information
        config_path = os.path.expanduser("~/projects/appt_reminder/conf/appt_reminder.config")
        parser.read(config_path, encoding="utf-8")

        print(f'has section mysql: {parser.has_section('mysql')}')

        # grab connection params
        mysql_user = parser.get('mysql', 'mysql_user')
        mysql_pass = parser.get('mysql', 'mysql_pass')
        mysql_host = parser.get('mysql', 'mysql_host')
        mysql_port = parser.get('mysql', 'mysql_port')
        mysql_dbname = parser.get('mysql', 'mysql_dbname')

        # BUILD CONNECTIO STRING
        # ======================
        # build connection string using params
        connection_string = f'mysql+pymysql://{mysql_user}:{mysql_pass}@{mysql_host}:{mysql_port}/{mysql_dbname}'
        print(f"connection string: {connection_string}")
        # pass string into engine
        engine = create_engine(connection_string, echo=True)
        g.engine = engine

def get_db():
    if 'db_session' not in g:
        engine = get_engine()
        Session = sessionmaker(bind=engine)
        g.db_session = Session()
    return g.db_session

Base = declarative_base()


# STUDENTS TABLE MAPPING
# ======================
class Students(Base):
    __tablename__ = 'STUDENTS'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email_address = Column(String(100), nullable=True, unique=True)
    phone_number = Column(String(13), nullable=False, unique=True)
    carrier = Column(String(25), nullable=False)
    enabled=Column(Boolean, default=True)
    
    # These are set by the trigger
    created_date = Column(DateTime, default=datetime.now())
    modified_date = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    messages = relationship("Message", back_populates="student")

# MESSAGES TABLE MAPPING
# ======================
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
    # This relates the MESSAGES table to the Student table
    student = relationship("Students", back_populates="messages")

# REMINDERS TABLE MAPPING
# =======================
class Reminder(Base):
    __tablename__ = 'LU_REMINDER'
    reminder_id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(50), nullable=False)
    # These are set by the trigger
    created_date = Column(DateTime, default=datetime.now(), nullable=False)
    modified_date = Column(DateTime, default=datetime.now(), onupdate=datetime.now())


# TEST CONNECTION TO DB