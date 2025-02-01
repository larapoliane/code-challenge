from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1
}

with DAG('extract_data', default_args=default_args, schedule_interval='@daily', catchup=True) as dag:

    extract_postgres = BashOperator(
        task_id='extract_postgres',
        bash_command='embulk run /workspaces/code-challenge/desafio_pipeline/configs/extract_postgres.yml'
    )

    extract_csv = BashOperator(
        task_id='extract_csv',
        bash_command='embulk run /workspaces/code-challenge/desafio_pipeline/configs/extract_csv.yml'
    )

    extract_postgres >> extract_csv
