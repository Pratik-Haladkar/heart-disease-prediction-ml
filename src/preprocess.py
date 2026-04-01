# src/preprocess.py

import pandas as pd


def load_data(path):
    """
    Load dataset and remove duplicates
    """
    df = pd.read_csv(path)

    # Remove duplicate rows (VERY IMPORTANT)
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]

    print(f"Removed {before - after} duplicate rows")
    print(f"Final dataset shape: {df.shape}")

    return df


def split_features_target(df):
    """
    Split dataset into features (X) and target (y)
    """
    X = df.drop("target", axis=1)
    y = df["target"]

    return X, y