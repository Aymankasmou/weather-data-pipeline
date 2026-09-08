from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.databricks.operators.databricks import (
    DatabricksRunNowOperator,
)

DATABRICKS_CONN_ID = "databricks_default"
JOB_ID = 807923737499034
default_args = {
    "owner": "airflow",
    "start_date": datetime(2026, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="orchestrate_weather_databricks_job",
    default_args=default_args,
    schedule="@daily",
    catchup=False,
) as dag:

    run_weather_pipeline = DatabricksRunNowOperator(
        task_id="trigger_databricks_weather_notebook",
        databricks_conn_id=DATABRICKS_CONN_ID,
        job_id=JOB_ID,
    )

    run_weather_pipeline