# src/evaluate.py

from sklearn.metrics import accuracy_score, classification_report
import joblib

def evaluate_model(X_test, y_test):
    model = joblib.load("models/model.pkl")

    y_pred = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))