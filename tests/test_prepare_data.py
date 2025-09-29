# tests/test_prepare_data.py

import sys
import os
import pandas as pd

# Ajouter le répertoire du projet au chemin de Python
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from prepare_data import prepare_data

def test_prepare_data():
    train_clean, test_clean = prepare_data()
    assert isinstance(train_clean, pd.DataFrame)
    assert isinstance(test_clean, pd.DataFrame)
    assert 'Survived' in train_clean.columns
    assert 'PassengerId' in test_clean.columns