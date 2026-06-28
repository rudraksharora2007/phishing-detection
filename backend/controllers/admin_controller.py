from flask import jsonify
from services.admin_service import get_stats, retrain_model


def stats():
    return jsonify(get_stats()), 200


def retrain():
    result = retrain_model()
    code = 200 if result["success"] else 500
    return jsonify(result), code
