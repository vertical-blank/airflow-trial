from datetime import timedelta

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.utils.dates import days_ago

def hoge_or_fuga(**kwargs):
    ti = kwargs['ti']
    task1_ret = ti.xcom_pull(key='k1')
    if task1_ret == 'hoge':
        return 'hoge_task'
    elif task1_ret == 'fuga':
        return 'fuga_task'
    else:
        return

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
with DAG(
    'control_flow',
    default_args=default_args,
    description='A simple control-flow DAG',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['example'],
) as dag:

    task1 = BashOperator(
        task_id='print',
        bash_command='echo "{{ ti.xcom_push(key="k1", value="hoge") }}"',
    )

    branch_task = BranchPythonOperator(
        task_id='branch_python',
        provide_context=True,
        python_callable=hoge_or_fuga
    )

    hoge_task = BashOperator(
        task_id='hoge_task',
        depends_on_past=False,
        bash_command='echo "hoge"'
    )

    fuga_task = BashOperator(
        task_id='fuga_task',
        depends_on_past=False,
        bash_command='echo "fuga"'
    )

    task1 >> branch_task >> hoge_task
    task1 >> branch_task >> fuga_task
