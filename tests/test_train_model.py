# tests/test_train_model.py

import sys
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Ajouter le répertoire du projet au chemin de Python
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from prepare_data import prepare_data
from train_model import train_model

def test_train_model():
    train_clean, _ = prepare_data()
    model = train_model(train_clean, "RandomForest")
    assert isinstance(model, RandomForestClassifier)

