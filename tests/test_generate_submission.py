# tests/test_generate_submission.py

import sys
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Ajouter le répertoire du projet au chemin de Python
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from prepare_data import prepare_data
from train_model import train_model
from main import generate_submission_if_needed

def test_generate_submission():
    train_clean, test_clean = prepare_data()
    model = train_model(train_clean, "RandomForest")  # Utiliser train_clean pour l'entraînement
    generate_submission_if_needed(model, test_clean)
    assert os.path.exists("submission.csv")
