import os
import logging

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from ingest_script import ingest_callable

default_args = {
    "owner": "airflow",
    "start_date": days_ago(250),
    "depends_on_past": False,
    "retries": 1,
}
#URL = '2021-02.parquet'
AIRFLOW_HOME = os.environ.get('AIRFLOW_HOME', '/opt/airflow/')
URL_PREFIX = 'https://d37ci6vzurychx.cloudfront.net/trip-data/'
URL_TEMPLATE = URL_PREFIX + 'yellow_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.parquet'
OUTPUT_FILE_TEMPLATE = AIRFLOW_HOME + '/output_{{ execution_date.strftime(\'%Y-%m\') }}.parquet'

PG_HOST = os.getenv('PG_HOST')
PG_USER = os.getenv('PG_USER')
PG_PASS = os.getenv('PG_PASS')
PG_PORT = os.getenv('PG_PORT')
PG_DATABASE = os.getenv('PG_DATABASE')
TABLE_NAME_TEMPLATE = 'yellow_taxi_{{ execution_date.strftime(\'%Y%m\') }}'

local_workflow = DAG(
    "LocalIngestionDag",
    default_args=default_args,
    schedule_interval="0 6 2 * *"
)

with local_workflow:
    wget_task = BashOperator(
        task_id='wget',
        # bash_command=f'curl -sSL {URL} > {AIRFLOW_HOME}/output.parquet'
        bash_command=f'curl -sSL {URL_TEMPLATE} > {OUTPUT_FILE_TEMPLATE}'
    )

    ingest_task = PythonOperator(
        task_id='ingest',
        python_callable=ingest_callable,
        op_kwargs=dict(
            user=PG_USER, 
            password=PG_PASS, 
            host=PG_HOST, 
            port=PG_PORT, 
            db=PG_DATABASE, 
            table_name=TABLE_NAME_TEMPLATE, 
            output_file=OUTPUT_FILE_TEMPLATE
        )
    )

    wget_task >>  ingest_task