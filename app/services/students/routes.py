from flask import Blueprint, jsonify, request
from app.services.students.action.student_action import StudentAction
from app.proj_utils.app_logger import info, error, debug

students_bp = Blueprint("students", __name__)
debug("student bp created")
action = StudentAction()
debug("connection created")

@students_bp.route("/students/<string:phone_number>", methods=["GET"])
def get_student(phone_number):
    debug("inside get_student view")
    student = action.get_student(phone_number)
    debug("student called by phone number")
    if student:
        debug("about to return json object to front end caller")
        return jsonify({
            "student_id": student.student_id,
            "firstname": student.firstname,
            "lastname": student.lastname,
            "phone_number": student.phone_number,
            "carrier": student.carrier,
            "email_address": student.email_address,
            "enabled" : student.enabled
        })
    else:
        error("unable to find student")
        return jsonify({"error": "Student not found"}), 404
    return jsonify({"message": ""})