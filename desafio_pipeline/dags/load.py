from airflow import DAG


with DAG('load_data', default_args=default_args, schedule_interval='@daily', catchup=True) as dag:

    load_postgres = BashOperator(
        task_id='load_postgres',
        bash_command='embulk run /workspaces/code-challenge/desafio_pipeline/configs/load_postgres.yml'
    )

    load_csv = BashOperator(
        task_id='load_csv',
        bash_command='embulk run /workspaces/code-challenge/desafio_pipeline/configs/load_csv.yml'
    )

    load_postgres >> load_csv
