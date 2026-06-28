from flask import request, jsonify, current_app, Response
from flask_jwt_extended import get_jwt_identity
from services.prediction_service import predict_and_log
from models.scan_model import ScanModel
from utils.security import sanitize_input, normalize_url
from utils.validators import validate_url_input
import csv
import io


def predict_url():
    data = request.get_json() or {}
    raw_url = sanitize_input(data.get("url", ""))
    url = normalize_url(raw_url)

    if not validate_url_input(url):
        return jsonify({"error": "Invalid URL"}), 400

    result = predict_and_log(get_jwt_identity(), url, current_app.config["VIRUSTOTAL_API_KEY"])
    return jsonify(result), 200


def get_history():
    scans = ScanModel.get_by_user(get_jwt_identity())
    payload = [
        {
            "id": str(s["_id"]),
            "url": s["url"],
            "result": s["result"],
            "confidence": s["confidence"],
            "explanation": s.get("explanation", []),
            "created_at": s["created_at"].isoformat(),
        }
        for s in scans
    ]
    return jsonify(payload), 200


def export_history_csv():
    scans = ScanModel.get_by_user(get_jwt_identity(), limit=500)
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["url", "result", "confidence", "timestamp"])
    for s in scans:
        writer.writerow([s["url"], s["result"], s["confidence"], s["created_at"].isoformat()])
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=scan_history.csv"},
    )
