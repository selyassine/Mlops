"""
Ce module contient les fonctions pour évaluer le modèle.
"""

from sklearn.metrics import accuracy_score


def evaluate_model(model, train_clean):
    """
    Évalue le modèle en calculant l'accuracy.
    """
    x = train_clean.drop("Survived", axis=1)
    y = train_clean["Survived"]
    preds = model.predict(x)
    return accuracy_score(y, preds)
