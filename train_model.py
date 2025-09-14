# train_model.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

DATA_PATH = os.path.join("data", "sample_emails.csv")
MODEL_PATH = "model.joblib"

def load_data(path=DATA_PATH):
    df = pd.read_csv(path)
    df = df.dropna(subset=["text","label"])
    return df

def train_and_save():
    df = load_data()
    X = df["text"].values
    y = df["label"].map(lambda s: 1 if s.strip().lower()=="phishing" else 0).values

    # If dataset is very small, stratify might fail; handle that
    try:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.25, random_state=42, stratify=y
        )
    except Exception:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.25, random_state=42
        )

    vect = TfidfVectorizer(ngram_range=(1,2), max_features=3000)
    clf = LogisticRegression(max_iter=1000)

    pipeline = make_pipeline(vect, clf)
    pipeline.fit(X_train, y_train)

    preds = pipeline.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds, target_names=["legitimate","phishing"]))

    joblib.dump(pipeline, MODEL_PATH)
    print(f"Saved model to {MODEL_PATH}")

if __name__ == "__main__":
    train_and_save()
