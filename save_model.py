"""
Ce module contient les fonctions pour sauvegarder le modèle.
"""

import joblib


def save_model(model, path="model.pkl"):
    """
    Sauvegarde le modèle dans un fichier.
    """
    joblib.dump(model, path)
