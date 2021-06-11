FROM apache/airflow:2.0.0

USER root

RUN apt-get update && \
    apt-get -y install sudo
RUN echo airflow:airflow | chpasswd && adduser airflow sudo

USER airflow

RUN airflow db init && \
    airflow users create \
    --username admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email yohei.yamana@syncthought.com \
    --password admin

# COPY airflow.cfg /opt/airflow/
COPY dags/* /opt/airflow/dags/

RUN airflow db init && \
    airflow users create \
    --username admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email yohei.yamana@syncthought.com \
    --password admin

RUN airflow dags unpause docker_dag
RUN airflow dags unpause tutorial
