from bson import ObjectId
from database.mongo import get_db


class ScanModel:
    @staticmethod
    def create(scan_data):
        result = get_db().scan_history.insert_one(scan_data)
        return str(result.inserted_id)

    @staticmethod
    def get_by_user(user_id, limit=50):
        cursor = get_db().scan_history.find({"user_id": ObjectId(user_id)}).sort("created_at", -1).limit(limit)
        return list(cursor)

    @staticmethod
    def count_all():
        return get_db().scan_history.count_documents({})
