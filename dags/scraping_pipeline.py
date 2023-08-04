from datetime import timedelta
from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'maxim',
    'depends_on_past': False,
    'email': ['maxim@becode.org'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'scraping_pipeline',
    default_args=default_args,
    schedule_interval='@daily', # Run every day at midnight
    start_date=days_ago(1),
)

dop = DockerOperator(
    docker_url='tcp://docker-proxy:2375',
    image='hln_scraper:latest',
    network_mode='bridge',
    task_id='task___scraper_hln',
    dag=dag,
)
