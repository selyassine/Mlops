# Titanic MLOps — pipeline CI/CD de bout en bout

**Un modèle de classification (Random Forest, jeu Kaggle Titanic) réentraîné, testé, conteneurisé et exécuté automatiquement à chaque `git push`, avec des outils libres et sans service cloud payant.**

[![ML Pipeline CI](https://github.com/selyassine/Mlops/actions/workflows/ci.yml/badge.svg)](https://github.com/selyassine/Mlops/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-GHCR-2496ED?logo=docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-CD-D24939?logo=jenkins&logoColor=white)
![Prefect](https://img.shields.io/badge/Prefect-orchestration-024DFD)
![Licence MIT](https://img.shields.io/badge/licence-MIT-green)

> Projet personnel d'apprentissage du MLOps. Le modèle est volontairement simple : l'objet du projet est la chaîne d'automatisation, pas la performance sur Titanic.

## Le pipeline

```
git push (main)
   │
   ▼
GitHub Actions ── lint (pylint) ── tests (pytest)  ── build de l'image ── push sur GHCR
   │                                                                        │
   └──── webhook ───────────────────────────────────────────────────────►  Jenkins
                                                                            │  build, tests dans le conteneur
                                                                            ▼
                                                                     Flow Prefect (réessais, logs, UI)
                                                                     préparer → entraîner → évaluer
                                                                     → sauvegarder → soumission
                                                                            │
                                                                            ▼
                                                           artefacts archivés : model.pkl, submission.csv
```

| Étape | Outil | Rôle |
| --- | --- | --- |
| Code | Python, scikit-learn | nettoyage, entraînement, évaluation (accuracy), fichier de soumission |
| Qualité | pylint, pytest | une fonction de test par étape du pipeline |
| Conteneur | Docker | même environnement en local, en CI et dans Jenkins |
| Intégration continue | GitHub Actions | tests, puis image publiée sur GitHub Container Registry (étiquettes `latest` et SHA du commit) |
| Déploiement continu | Jenkins | déclenché par webhook, exécute le flow dans le conteneur |
| Orchestration | Prefect | tâches avec réessais, suivi des exécutions dans l'interface |

## Lancer en local

```bash
git clone https://github.com/selyassine/Mlops.git && cd Mlops
python -m venv .venv && source .venv/bin/activate
make all          # installation, lint, préparation, entraînement, évaluation, sauvegarde, soumission
make test         # tests unitaires
```

Avec Prefect :

```bash
prefect server start                                       # interface sur http://127.0.0.1:4200
python deployment.py                                       # (autre terminal) sert le flow
prefect deployment run 'titanic-ml-pipeline/titanic-serve'
```

Avec l'image publiée :

```bash
docker run --rm -v "$(pwd)":/output ghcr.io/selyassine/titanic:latest \
  bash -c "python main.py --prepare_data --train_model --evaluate_model --save_model --generate_submission && cp model.pkl submission.csv /output/"
```

## Structure

```
.
├── prepare_data.py, train_model.py, evaluate_model.py,
│   save_model.py, load_model.py      # une étape du pipeline par module
├── main.py                           # point d'entrée en ligne de commande (une option par étape)
├── flows/pipeline_flow.py            # flow Prefect
├── deployment.py                     # déploiement Prefect
├── tests/                            # pytest
├── input/                            # données Kaggle Titanic
├── Dockerfile
├── Jenkinsfile
├── .github/workflows/ci.yml
└── Makefile
```

## Licence

Distribué sous licence MIT : voir [`LICENSE`](LICENSE).

---

Réalisé par **Yassine Selmi** — [github.com/selyassine](https://github.com/selyassine)
