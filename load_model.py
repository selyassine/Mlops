import joblib

def load_model(path="model.pkl"):
    return joblib.load(path)