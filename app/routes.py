from flask import Blueprint, request, jsonify
from .models import Student
from .database import SessionLocal

bp = Blueprint('main', __name__)

@bp.route('/students', methods=['GET'])
def get_students():
    session = SessionLocal()
    students = session.query(Student).all()
    session.close()
    return jsonify([s.to_dict() for s in students])

@bp.route('/students', methods=['POST'])
def create_student():
    session = SessionLocal()
    data = request.json
    student = Student(**data)
    session.add(student)
    session.commit()
    session.refresh(student)
    session.close()
    return jsonify(student.to_dict()), 201

def register_routes(app):
    app.register_blueprint(bp)
