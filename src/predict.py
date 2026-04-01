import numpy as np
import joblib

def predict(data):
    model = joblib.load("models/model.pkl")

    data = np.array(data).reshape(1, -1)
    prediction = model.predict(data)

    return prediction[0]