from database.engine import mysql_engine, SessionLocal
from sqlalchemy import text
from utils.app_logger import info
from database.models.students import Student
from database.models.messages import Message
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
            debug("about to create new student")
            with SessionLocal() as session:
                debug("inside with statement")
                new_student = Student(
                    firstname=firstname,
                    lastname=lastname,
                    email_address=email_address,
                    phone_number=phone_number,
                    carrier=carrier,
                    enabled=enabled
                )
                debug("new_student instantiated")
                session.add(new_student)
                debug("new_student added to session")
                session.commit()
                debug("commit attempted with new student. about to return him/her")
                return new_student
        except Exception as e:
            session.rollback()
            error("unable to create new student")
            raise e