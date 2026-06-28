from bson import ObjectId
from database.mongo import get_db


class UserModel:
    @staticmethod
    def create(user_data):
        result = get_db().users.insert_one(user_data)
        return str(result.inserted_id)

    @staticmethod
    def find_by_email(email):
        return get_db().users.find_one({"email": email})

    @staticmethod
    def find_by_id(user_id):
        return get_db().users.find_one({"_id": ObjectId(user_id)})
