from flows.pipeline_flow import pipeline_flow

if __name__ == "__main__":
    pipeline_flow.serve(
        name="titanic-serve",
        cron="0 * * * *",  # optionnel : toutes les heures
    )
