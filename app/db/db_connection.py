from db.engine import mysql_engine, SessionLocal
from sqlalchemy import text
from utils.app_logger import info
from db.models.students import Student
from db.models.messages import Message
from db.models.reminders import Reminder
from datetime import datetime
from utils.app_logger import debug, error

class Connection:

    def __init__(self):
        self.engine = mysql_engine
        info("shared engine created successfully")
    
    def test_db_connection(self):
        """
        Tests a connection to the database by generating a 'hello world' message with a SELECT statement. Prints that statement to the console.
        
        Args:
            No arguments.

        Returns:
            Nothing returned.

        Exceptions:
            Does not throw an exception."""
        with self.engine.connect() as conn:
            result = conn.execute(text("SELECT 'hello world'"))
            print(result.all())
    
    def create_student(self, firstname:str, lastname:str, email_address:str, phone_number:str, carrier:str, enabled:bool):
        """
        Creates a Student entity object for storage in the database.
        
        Args:
            firstname (str): the first name of the student.
            lastname (str): the last name of the student.
            email_address (str): the full email address of the student.
            phone_number (str): the phone number of the student in the form of (111)222-3333.
            carrier (str): the mobile carrier (Verizon, AT&T, US Cellular, etc.) of the student.
            enabled (bool): Whether the student has agreed to receive reminders.
        
        Returns:
            The newly-created Student entity object.
        
        Raises:
            Exception: If an error occurs during the student creation lifecycle."""
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
        """
        Retrieves a Student entity object. Finds the student with the student's phone number.
        
        Args:
            phone_number (str): the phone number of the student in the form of (111)222-3333.
        
        Returns:
            A Student entity object from the database.
        
        Raises:
            Exception: for any errors that occur during the student retreival lifecycle."""
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
        """
        Uses a student's phone number to remove a Student entity object from the database.
        
        Args:
            phone_number (str): the phone number of the student in the form of (111)222-3333.
        
        Returns:
            No return.
        
        Raises:
            Exception: for any errors during the student deletion lifecycle."""
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
        Creates a message for storage in the database. Messages are sent to or received from a person or group.  The session is rolled back if any errors occur during execution. 
        
        Args:
            student_id (int): the id of the student for whom the message is generated.
            subject (str): The subject field for the message.
            body (str): The contents of the message body.
            sent_at (datetime): The date the message was sent.
            direction (str): The direction (outgoing, incoming) of the message.
        
        Returns:
            The newly-generated Message entity object from the database.
        
        Raises:
            Exception: for any errors during the message creation lifecycle."""
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
        Retrieves Message entity objects from the database as a list. The session is rolled back if any errors occur during execution. 

        Args:
            student_id (int): The foreign key Message table's (FK) used to find all the messages to/from a particular student.
        
        Returns:
            messages (list): The list of Message entity objects for parsing.
        
        Raises:
            Exception: if an error occurs during the message retrieval lifecycle.
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
    
    def create_reminder(self, category:str, body:str):
        """
        Creates a new reminder for use in a message. For outgoing messages, reminders are put inside the message body. The transaction is rolledback if an error occurs during exection.
        
        Args:
            category (str): the type of reminder (drums, church, family, self, etc.)
            body (str): the reminder text.
        
        Returns:
            new_reminder (Reminder): a reminder entity object from the database.
        
        Raises:
            Exception: for any errors occuring during the reminder creation lifecycle."""
        try:
            with SessionLocal() as session:
                new_reminder = Reminder(
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
        """
        Deletes a reminder row from the database. Finds the target row by its category and body contents.
        
        Args:
            category (str): the type of reminder (drums, church, family, self, etc.)
            body (str): the reminder text.
        
        Returns:
            No return.
        
        Raises:
            Exception: for any errors occuring during the reminder deletion lifecycle.
            """
        try:
            del_reminder_msg = ""
            with SessionLocal() as session:
                reminder_to_delete = session.query(Reminder).filter_by(
                    category=category
                ).first()
                del_reminder_msg = f"Reminder id: {reminder_to_delete.reminder_id} successfully deleted."
                session.delete(reminder_to_delete)
                info(del_reminder_msg)
                session.commit()
        except Exception as e:
            session.rollback()
            error("unable to delete message")
            raise e