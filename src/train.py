# src/train.py

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from src.preprocess import load_data, split_features_target
import joblib


def train_model():
    df = load_data("data/heart.csv")

    # Use proper split function
    X, y = split_features_target(df)

    # Pipeline (prevents data leakage)
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", RandomForestClassifier(random_state=42))
    ])

    # Stratified Cross Validation (better for classification)
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    scores = cross_val_score(pipeline, X, y, cv=cv)

    print("Cross-validation accuracy:", scores.mean())

    # Train final model on full data
    pipeline.fit(X, y)

    # Save model
    joblib.dump(pipeline, "models/model.pkl")

    print("Model saved successfully!")


if __name__ == "__main__":
    train_model()