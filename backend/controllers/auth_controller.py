from flask import request, jsonify, current_app
from services.auth_service import AuthService
from utils.validators import validate_email_input
from utils.security import sanitize_input


def register():
    data = request.get_json() or {}
    email = sanitize_input(data.get("email", ""))
    password = data.get("password", "")

    if not validate_email_input(email):
        return jsonify({"error": "Invalid email format"}), 400
    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters"}), 400
    if len(password.encode("utf-8")) > 72:
        return jsonify({"error": "Password must be at most 72 bytes"}), 400

    payload, error = AuthService.register(email, password, current_app.config["ADMIN_EMAIL"])
    if error:
        return jsonify({"error": error}), 409
    return jsonify(payload), 201


def login():
    data = request.get_json() or {}
    email = sanitize_input(data.get("email", ""))
    password = data.get("password", "")

    if len(password.encode("utf-8")) > 72:
        return jsonify({"error": "Invalid credentials"}), 401

    payload, error = AuthService.login(email, password)
    if error:
        return jsonify({"error": error}), 401
    return jsonify(payload), 200
