from app.db.engine import Session
from sqlalchemy import text
from app.proj_utils.app_logger import error, info, debug
from app.models.students import Students
from app.services.students.domain.student import Student

class StudentAction:
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
            with Session.begin() as session:
                # define query
                query = text(f"SELECT * FROM STUDENTS WHERE phone_number = '{phone_number}'")
                   # , (phone_number,))
                student = session.execute(query).fetchone()
                
                debug(f"student: {student}")
                return student
        except Exception as e:
            session.rollback()
            error("unable to retrieve the student")
            raise e

    def create_student(self, content:dict):
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
            # TODO: add None type checks and other validation for attributes passed in
            # TODO: add a model that can be passed in as a single object instead of all these attributes
            with Session.begin() as session:
                new_student = Student(
                    _first_name=content["first_name"],
                    _last_name=content["last_name"],
                    _email_address=content["email_address"],
                    _phone_number=content["phone_number"],
                    _carrier=content["carrier"],
                    _enabled=content["enabled"]
                )
                # perform mapping here
                # new_students_instance = new_student.to_students()
                session.add(new_students_instance)
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
            with Session.begin() as session:
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