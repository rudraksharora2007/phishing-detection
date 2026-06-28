import subprocess
from database.mongo import get_db
from models.scan_model import ScanModel


def get_stats():
    db = get_db()
    users = db.users.count_documents({})
    scans = ScanModel.count_all()
    dangerous = db.scan_history.count_documents({"result": "Dangerous"})
    suspicious = db.scan_history.count_documents({"result": "Suspicious"})
    safe = db.scan_history.count_documents({"result": "Safe"})
    return {
        "total_users": users,
        "total_scans": scans,
        "risk_distribution": {
            "safe": safe,
            "suspicious": suspicious,
            "dangerous": dangerous,
        },
    }


def retrain_model():
    proc = subprocess.run(
        ["python", "ml/train_model.py", "--dataset", "ml/dataset/sample_urls.csv", "--output", "ml/phishing_model.pkl"],
        capture_output=True,
        text=True,
    )
    return {"success": proc.returncode == 0, "stdout": proc.stdout, "stderr": proc.stderr}
