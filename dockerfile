# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Copier requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet
COPY . .

# Entry point : ton flow Prefect
CMD ["python", "flows/pipeline_flow.py"]

