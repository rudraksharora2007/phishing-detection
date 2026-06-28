import argparse
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from feature_extractor import FEATURE_COLUMNS


def train(dataset_path: str, output_path: str):
    data = pd.read_csv(dataset_path)
    x = data[FEATURE_COLUMNS]
    y = data["label"]

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(n_estimators=250, random_state=42, class_weight="balanced")
    model.fit(x_train, y_train)

    preds = model.predict(x_test)
    print("Accuracy:", round(accuracy_score(y_test, preds), 4))
    print(classification_report(y_test, preds))

    joblib.dump(model, output_path)
    print(f"Model saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="ml/dataset/sample_urls.csv")
    parser.add_argument("--output", default="ml/phishing_model.pkl")
    args = parser.parse_args()
    train(args.dataset, args.output)
