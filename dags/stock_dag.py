from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

sys.path.append("/opt/airflow/scripts")
from fetch_data import fetch_and_store


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "stock_pipeline",
    default_args=default_args,
    description="Fetch and store stock data in PostgreSQL",
    schedule_interval="@hourly",  
    catchup=False,
) as dag:

    fetch_and_store_task = PythonOperator(
        task_id="fetch_and_store_task",
        python_callable=fetch_and_store
    )

    fetch_and_store_task
