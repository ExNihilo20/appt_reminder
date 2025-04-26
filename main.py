from utils.app_logger import debug
from database.connection import Connection



def main():
    debug("about to get connection")
    conn = Connection()
    debug("about to test connection")
    conn.test_db_connection()
    debug("about to create new student")
    # new_student = conn.create_student("firstname", "last_name", "firstname.lastname@protonmail.com", "111-222-3333", "Verizon", False)
    debug("about to print new student")
    # print(new_student.student_id, new_student.firstname)
    conn.drop_student("111-222-3333")
    

main()