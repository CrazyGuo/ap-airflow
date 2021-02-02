from datetime import datetime
import os

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator


default_args = {
    "owner": "huanhuan.guo",
    "start_date": datetime(2021, 1, 26)
}

dag = DAG("first_example_dag", 
        description="test bash command",
        default_args=default_args, 
        catchup=False,
        schedule_interval='*/5 * * * *')


t1 = BashOperator(task_id="first_example_task", bash_command="date", retries=0, dag=dag)