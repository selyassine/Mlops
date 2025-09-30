# flows/pipeline_flow.py
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from prefect import flow, task
from prefect.blocks.notifications import SlackWebhook
from prepare_data import prepare_data
from train_model import train_model
from evaluate_model import evaluate_model
from save_model import save_model
import joblib

@task(retries=2, retry_delay_seconds=30)
def task_prepare_data():
    return prepare_data()

@task
def task_train(train_clean, model_name="RandomForest"):
    model = train_model(train_clean, model_name)
    return model

@task
def task_evaluate(model, train_clean):
    return evaluate_model(model, train_clean)

@task
def task_save(model, path="model.pkl"):
    save_model(model, path)
    return path

@flow(name="titanic-ml-pipeline")
def pipeline_flow(model_name="RandomForest"):
    train_clean, test_clean = task_prepare_data()
    model = task_train(train_clean, model_name)
    acc = task_evaluate(model, train_clean)
    path = task_save(model)
    # Optionally notify on Slack
    # SlackWebhook.load("my-slack").send_message(f"Pipeline done. Acc={acc:.3f}")
    return {"model_path": path, "accuracy": acc}

if __name__ == "__main__":
    pipeline_flow()