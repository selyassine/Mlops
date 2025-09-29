# Makefile pour automatiser les tâches du projet

# Installation des dépendances
install:
	pip install -r requirements.txt

# Vérification du code
check:
	pylint main.py prepare_data.py train_model.py evaluate_model.py save_model.py
	black --check main.py prepare_data.py train_model.py evaluate_model.py save_model.py
	flake8 main.py prepare_data.py train_model.py evaluate_model.py save_model.py

# Formatter le code
format:
	black main.py prepare_data.py train_model.py evaluate_model.py save_model.py

# Préparation des données
prepare_data:
	python main.py --prepare_data

# Entraîner le modèle
train_model:
	python main.py --train_model --model RandomForest

# Évaluer le modèle
evaluate_model:
	python main.py --evaluate_model --model RandomForest

# Sauvegarder le modèle
save_model:
	python main.py --save_model --model RandomForest

# Générer la soumission
generate_submission:
	python main.py --generate_submission --model RandomForest

# Exécuter les tests unitaires avec pytest
test:
	pytest tests/

# Automatiser toutes les tâches
all: install check prepare_data train_model evaluate_model save_model generate_submission

# Raccourcis pour les tâches spécifiques
train:
	python main.py --train_model --model RandomForest

evaluate:
	python main.py --evaluate_model --model RandomForest

submission:
	python main.py --generate_submission --model RandomForest
