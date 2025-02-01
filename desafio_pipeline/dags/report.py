import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1
}

def generate_report(ds, **kwargs):
    import psycopg2

    conn = psycopg2.connect(host="localhost", database="final_db", user="postgres", password="postgres")
    query = """
        SELECT o.order_id, o.customer_id, o.order_date, od.product_id, od.quantity
        FROM orders o
        JOIN order_details od ON o.order_id = od.order_id;
    """
    df = pd.read_sql(query, conn)
    df.to_csv(f"/data/reports/{ds}.csv", index=False)
    df.to_json(f"/data/reports/{ds}.json", orient="records")

with DAG('generate_report', default_args=default_args, schedule_interval='@daily', catchup=True) as dag:

    generate_report_task = PythonOperator(
        task_id='generate_report',
        python_callable=generate_report
    )

    generate_report_task
