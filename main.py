"""
Ce module contient le pipeline principal du projet Titanic.
"""

import argparse
import pandas as pd
from prepare_data import prepare_data
from train_model import train_model
from evaluate_model import evaluate_model
from save_model import save_model


def prepare_data_if_needed(train_clean, test_clean):
    """
    Prépare les données si elles ne sont pas déjà préparées.
    """
    if train_clean is None or test_clean is None:
        print("Préparation des données...")
        train_clean, test_clean = prepare_data()
    return train_clean, test_clean


def train_model_if_needed(train_clean, model_name):
    """
    Entraîne le modèle si nécessaire.
    """
    if train_clean is None:
        train_clean, _ = prepare_data()
    print("Entraînement du modèle...")
    return train_model(train_clean, model_name)


def evaluate_model_if_needed(model, train_clean):
    """
    Évalue le modèle si nécessaire.
    """
    if train_clean is None:
        train_clean, _ = prepare_data()
    if model is None:
        model = train_model(train_clean, "RandomForest")
    print("Évaluation...")
    acc = evaluate_model(model, train_clean)
    print(f"Accuracy : {acc:.2f}")


def save_model_if_needed(model):
    """
    Sauvegarde le modèle si nécessaire.
    """
    if model is None:
        train_clean, _ = prepare_data()
        model = train_model(train_clean, "RandomForest")
    print("Sauvegarde du modèle...")
    save_model(model)


def generate_submission_if_needed(model, test_clean):
    """ 
    Génère la soumission si nécessaire.
    """
    if test_clean is None:
        _, test_clean = prepare_data()
    if model is None:
        train_clean, _ = prepare_data()
        model = train_model(train_clean, "RandomForest")
    print("Génération de la soumission...")
    x_test = test_clean.drop("PassengerId", axis=1)
    preds = model.predict(x_test)
    submission = pd.DataFrame({"PassengerId": test_clean["PassengerId"], "Survived": preds})
    submission.to_csv("submission.csv", index=False)
    print("Soumission sauvegardée : submission.csv")


def main():
    """
    Pipeline principal pour entraîner et évaluer le modèle.
    """
    parser = argparse.ArgumentParser(description="Titanic ML Pipeline")
    parser.add_argument("--model", default="RandomForest", help="Modèle à entraîner")
    parser.add_argument("--prepare_data", action="store_true", help="Préparer les données")
    parser.add_argument("--train_model", action="store_true", help="Entraîner le modèle")
    parser.add_argument("--evaluate_model", action="store_true", help="Évaluer le modèle")
    parser.add_argument("--save_model", action="store_true", help="Sauvegarder le modèle")
    parser.add_argument("--generate_submission", action="store_true", help="Générer la soumission")
    args = parser.parse_args()

    train_clean = None
    test_clean = None
    model = None

    if args.prepare_data:
        train_clean, test_clean = prepare_data()

    if args.train_model:
        model = train_model_if_needed(train_clean, args.model)

    if args.evaluate_model:
        evaluate_model_if_needed(model, train_clean)

    if args.save_model:
        save_model_if_needed(model)

    if args.generate_submission:
        generate_submission_if_needed(model, test_clean)


if __name__ == "__main__":
    main()
