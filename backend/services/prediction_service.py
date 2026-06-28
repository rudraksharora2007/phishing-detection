from datetime import datetime
from bson import ObjectId
from models.scan_model import ScanModel
from ml.predict import Predictor
from services.virustotal_service import check_virustotal

predictor = Predictor()


def map_risk(prediction: int, phishing_probability: float):
    if prediction == 1 and phishing_probability >= 0.8:
        return "Dangerous"
    if prediction == 1 and phishing_probability >= 0.55:
        return "Suspicious"
    return "Safe"


def explain(features: dict):
    reasons = []
    if features["uses_https"] == 0:
        reasons.append("No HTTPS detected")
    if features["special_char_count"] > 6:
        reasons.append("Excessive special characters")
    if features["suspicious_keyword_count"] > 0:
        reasons.append("Contains suspicious keywords")
    if features["has_ip"] == 1:
        reasons.append("Uses IP address in URL")
    if features["domain_age_days"] != -1 and features["domain_age_days"] < 180:
        reasons.append("Recently registered domain")
    return reasons or ["No major phishing indicators detected"]


def predict_and_log(user_id: str, url: str, vt_api_key: str):
    prediction, confidence, phishing_probability, features = predictor.predict_url(url)
    risk = map_risk(prediction, phishing_probability)
    reasons = explain(features)
    vt = check_virustotal(url, vt_api_key)

    result = {
        "url": url,
        "prediction": int(prediction),
        "confidence": round(confidence * 100, 2),
        "phishing_probability": round(phishing_probability * 100, 2),
        "risk_level": risk,
        "explanation": reasons,
        "features": features,
        "virustotal": vt,
    }

    ScanModel.create(
        {
            "user_id": ObjectId(user_id),
            "url": url,
            "result": risk,
            "confidence": result["confidence"],
            "explanation": reasons,
            "created_at": datetime.utcnow(),
        }
    )
    return result
