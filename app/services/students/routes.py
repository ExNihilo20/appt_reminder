from flask import Blueprint, jsonify, request
from app.services.students.action.student_action import StudentAction
from app.proj_utils.app_logger import info, error, debug
from app.models.students import Students

students_bp = Blueprint("students", __name__)
debug("student bp created")
action = StudentAction()
debug("connection created")

@students_bp.route("/students/<string:phone_number>", methods=["GET"])
def get_student(phone_number):
    debug("inside get_student view")
    student = action.get_student(phone_number)
    debug("student called by phone number")
    try:
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
    except AttributeError as e:
        error("incorrect phone number entered")
        return jsonify({"message": "No student exists for this phone number"}, 404)
    

@students_bp.route("/students", methods=["POST"])
def create_student():
    debug("inside create_student view")
    debug("student called by phone number")
    try:
        debug("about to return json object to front end caller")
        post_body = request.json
        student = action.create_student(post_body)
        return jsonify(student)
    except:
        error("error during student creation")
        return jsonify({"message": "error during student creation"}, 404)