from database.engine import mysql_engine, SessionLocal
from sqlalchemy import text
from utils.app_logger import info
from database.models.students import Student
from database.models.messages import Message
from database.models.reminders import Reminder
from datetime import datetime
from utils.app_logger import debug, error

class Connection:
    def __init__(self):
        self.engine = mysql_engine
        info("shared engine created successfully")
    
    def test_db_connection(self):
        with self.engine.connect() as conn:
            result = conn.execute(text("SELECT 'hello world'"))
            print(result.all())
    
    def create_student(self, firstname:str, lastname:str, email_address:str, phone_number:str, carrier:str, enabled:bool):
        try:
            with SessionLocal() as session:
                new_student = Student(
                    firstname=firstname,
                    lastname=lastname,
                    email_address=email_address,
                    phone_number=phone_number,
                    carrier=carrier,
                    enabled=enabled
                )
                session.add(new_student)
                session.commit()
                session.refresh(new_student) # remove if not returning student
                return new_student
        except Exception as e:
            session.rollback()
            error("unable to create new student")
            raise e
    
    def get_student(self, phone_number:str):
        try:
            with SessionLocal() as session:
                searched_student = session.query(Student).filter_by(
                    phone_number=phone_number
                ).first()
                return searched_student
        except Exception as e:
            session.rollback()
            error("unable to create new student")
            raise e
        
    def drop_student(self, phone_number:str):
        try:
            del_student_msg = ""
            with SessionLocal() as session:
                student_to_delete = session.query(Student).filter_by(
                    phone_number=phone_number
                ).first()
                del_student_msg = f"Student {student_to_delete.lastname}, {student_to_delete.firstname} (id: {student_to_delete.student_id}) successfully deleted."
                session.delete(student_to_delete)
                info(del_student_msg)
                session.commit()
        except Exception as e:
            session.rollback()
            error("unable to delete student")
            raise e
        
    def create_message(self, student_id:int, subject:str, body:str, sent_at:datetime, direction:str):
        """
        Creates a message based on a student id.
        
        Args:
            student_id (int): the id of the student for whom the message is generated.
            subject (str): The subject field for the message.
            body (str): The contents of the message body.
            sent_at (datetime): The date the message was sent.
            direction (str): The direction (outgoing, incoming) of the message."""
        try:
            with SessionLocal() as session:
                message = Message
                new_message = Message(
                    student_id=student_id,
                    subject=subject,
                    body=body,
                    sent_at=sent_at,
                    direction=direction
                )
                create_success_msg = f"Message id: {message.message_id} successfully created"
                session.add(new_message)
                session.commit()
                info(create_success_msg)
                session.refresh(new_message)
                return new_message
        except Exception as e:
            session.rollback()
            error("unable to create new message")
            raise e
    
    def get_messages(self, student_id:int) -> list:
        """
        Retrieves messages from the database as a list. The session is rolled back if any errors occur during execution.

        Args:
            student_id (int): The foreign key (FK) used to find the messages.
        
        Returns:
            messages (list): The list of messages for parsing.
        
        Raises:
            Exception: if an error occurs during exection.
        """
        try:
            retrieved_messages = ""
            with SessionLocal() as session:
                messages = session.query(Message).filter_by(
                    student_id=student_id
                ).all()
                retrieved_messages = f"Retrieved {len(messages)} messages."
                info(retrieved_messages)
                return messages
        except Exception as e:
            session.rollback()
            error("unable to delete message")
            raise e
    
    def create_reminder(self, reminder_id:int, category:str, body:str):
        try:
            with SessionLocal() as session:
                new_reminder = Reminder(
                    student_id=reminder_id,
                    category=category,
                    body=body,
                )
                session.add(new_reminder)
                session.commit()
                session.refresh(new_reminder) # remove if not returning student
                return new_reminder
        except Exception as e:
            session.rollback()
            error("unable to create new reminder")
            raise e
    
    def drop_reminder(self, category:str, body:str):
        try:
            del_reminder_msg = ""
            with SessionLocal() as session:
                reminder_to_delete = session.query(Reminder).filter_by(
                    category=category,
                    body=body
                ).first()
                del_reminder_msg = f"Reminder id: {reminder_to_delete.reminder_id} successfully deleted."
                session.delete(reminder_to_delete)
                info(del_reminder_msg)
                session.commit()
        except Exception as e:
            session.rollback()
            error("unable to delete message")
            raise e