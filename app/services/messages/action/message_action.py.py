from app.db.engine import Session
from sqlalchemy import select
from app.proj_utils.app_logger import error, info
from app.models.messages import Message
from datetime import datetime


class MessageAction:
    def __init__(self):
        pass

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
            with Session.begin() as session:
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
    
    def get_messages(self, student_identifier:int) -> list:
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
            with Session.begin() as session:
                # TODO: VERIFY 
                # use the select statement to build query statement
                messages = session.execute(
                    select(Message).filter_by(
                        student_id=student_identifier
                    )
                ).scalars().all()
                # statement = select(Message).filter_by(
                #     student_id=student_id
                # )
                # # get a list of messages
                # messages = session.scalars(statement).all()
                retrieved_messages = f"Retrieved {len(messages)} messages."
                info(retrieved_messages)
                return messages
        except Exception as e:
            session.rollback()
            error("unable to delete message")
            raise e
