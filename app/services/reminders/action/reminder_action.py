from app.db.engine import Session
from app.proj_utils.app_logger import error, info
from app.models.reminders import Reminder

class ReminderAction:
    def __init__(self):
        pass

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
            with Session() as session:
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
            with Session() as session:
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