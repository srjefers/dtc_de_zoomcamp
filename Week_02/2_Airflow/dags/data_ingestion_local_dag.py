import os
import logging

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "depends_on_past": False,
    "retries": 1,
}

local_workflow = DAG(
    "LocalIngestionDag",
    default_args=default_args,
    schedule_interval="0 6 2 * *"
)


with local_workflow:
    wget_task = BashOperator(
        task_id='wget',
        bash_command='echo "Hello world"'
    )

    ingest_task = BashOperator(
        task_id='ingest',
        bash_command='pwd'
    )

    wget_task >>  ingest_task