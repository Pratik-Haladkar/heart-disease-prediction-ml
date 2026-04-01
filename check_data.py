import pandas as pd

df = pd.read_csv("data/heart.csv")

print("Shape:", df.shape)
print("\nTarget Distribution:")
print(df["target"].value_counts())
print("\nDuplicate Rows:", df.duplicated().sum())