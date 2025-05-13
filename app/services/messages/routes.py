from flask import Blueprint, jsonify, request
from db.db_connection import Connection

messages_bp = Blueprint("messages", __name__)

@messages_bp.route("/messages", methods=["GET"])
def get_message():
    messages = 
    return jsonify({"message": ""})