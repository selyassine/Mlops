
 Titanic MLOps Pipeline (100 % local & gratuit)

Entraînement automatisé d’un modèle RandomForest sur les données Titanic → à chaque git push.



 Ce que fait ce projet


Étape			Outil				Résultat
Code			Python				nettoyage, entraînement, évaluation, soumission
Container		Docker				même environnement partout
CI			GitHub Actions			build & push image GHCR
CD			Jenkins				pull image & lance Prefect
Orchestration		Prefect OSS			logs, retries, UI
Artefacts		Jenkins				model.pkl + submission.csv archivés






 Test rapide (local)


1. Lancer le serveur Prefect

prefect server start

2. Servir le flow

python deployment.py

3. Lancer un run

prefect deployment run 'titanic-ml-pipeline/titanic-serve'

OU

make all






 Test Docker (image publique)

Sans Prefect :

docker run --rm -v $(pwd):/output ghcr.io/selyassine/titanic:latest bash -c "python main.py --all && cp model.pkl submission.csv /output/"

Avec Prefect (serveur local requis) :

docker run --rm --network host -e PREFECT_API_URL=http://127.0.0.1:4200/api
 -v $(pwd):/output ghcr.io/selyassine/titanic:latest






 Pipeline complet (auto)

Push sur main

GitHub Actions build & push l’image

Jenkins reçoit le webhook, pull l’image, lance le flow

Prefect UI : http://127.0.0.1:4200

Artefacts : model.pkl + submission.csv dans Jenkins





 Image Docker

Image publique : https://ghcr.io/selyassine/titanic:latest

docker pull ghcr.io/selyassine/titanic:latest





 Structure

.
├── flows/pipeline_flow.py # flow Prefect
├── src/ # modules ML
├── tests/ # pytest
├── Dockerfile # image
├── Jenkinsfile # pipeline Jenkins
├── .github/workflows/ci.yml # pipeline GitHub
├── requirements.txt # dépendances
└── README.md # ce fichier





Pré-requis local

Docker

Python 3.10+

Prefect OSS (pip install prefect)





Auteur

Yassine – pipeline 100 % local, zéro cloud payant.
