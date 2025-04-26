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