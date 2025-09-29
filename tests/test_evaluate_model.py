# tests/test_evaluate_model.py

import sys
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Ajouter le répertoire du projet au chemin de Python
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from prepare_data import prepare_data
from train_model import train_model
from evaluate_model import evaluate_model

def test_evaluate_model():
    train_clean, _ = prepare_data()
    model = train_model(train_clean, "RandomForest")
    acc = evaluate_model(model, train_clean)
    assert isinstance(acc, float)
    assert 0 <= acc <= 1

