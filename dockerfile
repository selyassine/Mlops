# Dockerfile
FROM python:3.12-slim

# Définir le répertoire de travail dans le container
WORKDIR /app

# Copier uniquement requirements d'abord pour profiter du cache Docker
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet dans le container
COPY . .

# Optionnel : s'assurer que tous les scripts sont exécutables
RUN chmod -R 755 /app

# Commande par défaut : exécuter le flow Prefect
CMD ["python", "flows/pipeline_flow.py"]
