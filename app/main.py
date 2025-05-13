from app.utils.app_logger import debug
from app.db.db_connection import Connection
from datetime import datetime
from flask import Flask
from app.services.students import student_service


app = Flask(__name__)

@app.route("/students", methods=["GET"])
def get_students():
    
    pass

def main():
    debug("about to get connection")
    conn = Connection()
    # debug("about to test connection")
    # conn.test_db_connection()
    # debug("about to create new student")
    student = conn.get_student('111-222-3333')
    message = conn.create_message(str(student.student_id),
                                  "drum lessons",
                                  "You have a drum lesson tomorrow at 10AM",
                                  datetime(2025,5,2), 'outgoing')
    print(message)
    reminder = conn.create_reminder("drum lessons", "This is a reminder that you have a drum lesson tomorrow")
    print(reminder)
    # new_student = conn.create_student("firstname", "last_name", "firstnamess.lastname@protonmail.com", "111-222-3333", "Verizon", False)
    debug("about to print new student")
    # print(new_student.student_id, new_student.firstname)
    # conn.drop_student("111-222-3333")
    # new_message = conn.create_message()
    

main()