"""
Ce module contient les fonctions pour préparer les données du projet Titanic.
"""

import pandas as pd
import numpy as np


def prepare_data():
    """
    Prépare les données en effectuant le nettoyage et la transformation nécessaires.
    """
    train_df = pd.read_csv("input/train.csv")
    test_df = pd.read_csv("input/test.csv")
    combine = [train_df.copy(), test_df.copy()]

    for dataset in combine:
        dataset["Title"] = dataset.Name.str.extract(r" ([A-Za-z]+)\.", expand=False)
        dataset["Title"] = dataset["Title"].replace(
            [
                "Lady",
                "Countess",
                "Capt",
                "Col",
                "Don",
                "Dr",
                "Major",
                "Rev",
                "Sir",
                "Jonkheer",
                "Dona",
            ],
            "Rare",
        )
        dataset["Title"] = (
            dataset["Title"].replace("Mlle", "Miss").replace("Ms", "Miss").replace("Mme", "Mrs")
        )
        title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}
        dataset["Title"] = dataset["Title"].map(title_mapping).fillna(0)

        dataset["Sex"] = dataset["Sex"].map({"female": 1, "male": 0}).astype(int)

        guess_ages = np.zeros((2, 3))
        for i in range(2):
            for j in range(3):
                guess_df = dataset[(dataset["Sex"] == i) & (dataset["Pclass"] == j + 1)][
                    "Age"
                ].dropna()
                guess_ages[i, j] = guess_df.median()
                dataset.loc[
                    (dataset.Age.isnull()) & (dataset.Sex == i) & (dataset.Pclass == j + 1), "Age"
                ] = guess_ages[i, j]
        dataset["Age"] = dataset["Age"].astype(int)

        dataset.loc[dataset["Age"] <= 16, "Age"] = 0
        dataset.loc[(dataset["Age"] > 16) & (dataset["Age"] <= 32), "Age"] = 1
        dataset.loc[(dataset["Age"] > 32) & (dataset["Age"] <= 48), "Age"] = 2
        dataset.loc[(dataset["Age"] > 48) & (dataset["Age"] <= 64), "Age"] = 3
        dataset.loc[dataset["Age"] > 64, "Age"] = 4

        freq_port = dataset.Embarked.dropna().mode()[0]
        dataset["Embarked"] = dataset["Embarked"].fillna(freq_port)
        dataset["Embarked"] = dataset["Embarked"].map({"S": 0, "C": 1, "Q": 2}).astype(int)

        dataset["Fare"] = dataset["Fare"].fillna(dataset["Fare"].dropna().median())
        dataset.loc[dataset["Fare"] <= 7.91, "Fare"] = 0
        dataset.loc[(dataset["Fare"] > 7.91) & (dataset["Fare"] <= 14.454), "Fare"] = 1
        dataset.loc[(dataset["Fare"] > 14.454) & (dataset["Fare"] <= 31), "Fare"] = 2
        dataset.loc[dataset["Fare"] > 31, "Fare"] = 3
        dataset["Fare"] = dataset["Fare"].astype(int)

        dataset["FamilySize"] = dataset["SibSp"] + dataset["Parch"] + 1
        dataset["IsAlone"] = 0
        dataset.loc[dataset["FamilySize"] == 1, "IsAlone"] = 1

    train_clean = combine[0].drop(
        ["Name", "PassengerId", "Ticket", "Cabin", "SibSp", "Parch", "FamilySize"], axis=1
    )
    test_clean = combine[1].drop(
        ["Name", "Ticket", "Cabin", "SibSp", "Parch", "FamilySize"], axis=1
    )

    print("Succès : données préparées")
    return train_clean, test_clean
