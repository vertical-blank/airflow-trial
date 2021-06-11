
from datetime import timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
with DAG(
    'docker_dag', 
    default_args=default_args, 
    schedule_interval="*/5 * * * *", 
    start_date=days_ago(2),
    catchup=False,
    tags=['docker'],
) as dag:
    t1 = BashOperator(
        task_id='print_current_date',
        bash_command='date'
    )
    t2 = DockerOperator(
        task_id='docker_command',
        image='hello-world:latest',
        api_version='auto',
        auto_remove=True,
        do_xcom_push=False,
        # command="/bin/sleep 30",
        # docker_url="unix://var/run/docker.sock",
        # network_mode="bridge"
    )
    t3 = BashOperator(
        task_id='print_hello',
        bash_command='echo "hello world"'
    )
    t1 >> t2 >> t3
