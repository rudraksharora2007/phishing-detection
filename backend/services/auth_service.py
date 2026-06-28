from datetime import datetime
from passlib.hash import bcrypt
from flask_jwt_extended import create_access_token
from models.user_model import UserModel


class AuthService:
    @staticmethod
    def register(email, password, admin_email):
        if UserModel.find_by_email(email):
            return None, "User already exists"

        user_id = UserModel.create(
            {
                "email": email,
                "password": bcrypt.hash(password),
                "is_admin": email == admin_email,
                "created_at": datetime.utcnow(),
            }
        )
        token = create_access_token(identity=user_id)
        return {"token": token, "user": {"email": email, "is_admin": email == admin_email}}, None

    @staticmethod
    def login(email, password):
        user = UserModel.find_by_email(email)
        if not user or not bcrypt.verify(password, user["password"]):
            return None, "Invalid credentials"
        token = create_access_token(identity=str(user["_id"]))
        return {"token": token, "user": {"email": user["email"], "is_admin": user.get("is_admin", False)}}, None
