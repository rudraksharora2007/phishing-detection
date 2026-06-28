from flask import Blueprint
from flask_jwt_extended import jwt_required
from controllers.predict_controller import predict_url, get_history, export_history_csv

predict_bp = Blueprint("predict", __name__)

predict_bp.post("/predict")(jwt_required()(predict_url))
predict_bp.get("/history")(jwt_required()(get_history))
predict_bp.get("/history/export")(jwt_required()(export_history_csv))
