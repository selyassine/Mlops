"""
Ce module contient les fonctions pour entraîner le modèle.
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier


def train_model(train_clean, model_name="RandomForest"):
    """
    Entraîne le modèle spécifié.
    """
    x = train_clean.drop("Survived", axis=1)
    y = train_clean["Survived"]

    models = {
        "LogisticRegression": LogisticRegression(),
        "RandomForest": RandomForestClassifier(n_estimators=100),
        "SVC": SVC(),
        "KNN": KNeighborsClassifier(n_neighbors=3),
        "NaiveBayes": GaussianNB(),
        "DecisionTree": DecisionTreeClassifier(),
    }

    model = models[model_name]
    model.fit(x, y)
    return model
