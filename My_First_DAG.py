#This is my first basic DAG with single bash operator and python task.
from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

with DAG(dag_id='my_first_dag', start_date=datetime(2024,6,23), schedule='0 0 * * *') as my_first_dag:
    hello = BashOperator(task_id="hello", bash_command="echo hello fom bash operator!")

    @task()
    def hello_task():
        print("This is my first python task")

    hello_task() >> hello
