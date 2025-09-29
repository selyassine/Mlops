# tests/test_save_model.py

import sys
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Ajouter le répertoire du projet au chemin de Python
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from prepare_data import prepare_data
from train_model import train_model
from save_model import save_model

def test_save_model():
    train_clean, _ = prepare_data()
    model = train_model(train_clean, "RandomForest")
    save_model(model)
    assert os.path.exists("model.pkl")
    loaded_model = joblib.load("model.pkl")
    assert isinstance(loaded_model, RandomForestClassifier)

