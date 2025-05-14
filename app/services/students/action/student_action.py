from app.db.engine import Session
from app.proj_utils.app_logger import error
from app.models.students import Student

class StudentService:
    def __init__(self):
        pass



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
            with Session() as session:
                searched_student = session.query(Student).filter_by(
                    phone_number=phone_number
                ).first()
                return searched_student
        except Exception as e:
            session.rollback()
            error("unable to create new student")
            raise e

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
            with Session as session:
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
            with Session() as session:
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