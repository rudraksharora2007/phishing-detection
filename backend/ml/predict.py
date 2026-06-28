import joblib
import pandas as pd
from ml.feature_extractor import extract_features, FEATURE_COLUMNS


class Predictor:
    def __init__(self, model_path="ml/phishing_model.pkl"):
        self.model = joblib.load(model_path)

    def predict_url(self, url: str):
        features = extract_features(url)
        frame = pd.DataFrame([[features[c] for c in FEATURE_COLUMNS]], columns=FEATURE_COLUMNS)
        prediction = int(self.model.predict(frame)[0])
        probs = self.model.predict_proba(frame)[0]
        confidence = float(max(probs))
        phishing_probability = float(probs[1]) if len(probs) > 1 else confidence
        return prediction, confidence, phishing_probability, features
