from flask import Blueprint
from controllers.admin_controller import stats, retrain
from middleware.auth import admin_required

admin_bp = Blueprint("admin", __name__)

admin_bp.get("/stats")(admin_required(stats))
admin_bp.post("/retrain")(admin_required(retrain))
