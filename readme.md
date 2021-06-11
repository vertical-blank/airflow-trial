
```bash
docker build . -t airflow:latest
```

```bash
docker-compose up
```

DockerOperator定義
https://airflow.apache.org/docs/apache-airflow-providers-docker/stable/_api/airflow/providers/docker/operators/docker/index.html#module-airflow.providers.docker.operators.docker

baseoperator定義
https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/baseoperator/index.html

今回はホストのDockerをmountで無理やり叩いているが、リモートのDockerで動かしたい場合はこれで出来そう

```
docker_url: str = 'unix://var/run/docker.sock',
```

DAG定義
https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/dag/index.html

参考
https://rinoguchi.net/2020/11/airflow-dockeroperator.html
https://marclamberti.com/blog/how-to-use-dockeroperator-apache-airflow/
https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#users
