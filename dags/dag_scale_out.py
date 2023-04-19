from __future__ import annotations

import pendulum

from airflow import DAG

from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

with DAG(
        "dag_scale_out",
        default_args={"retries": 1},
        description="DAG tutorial",
        schedule="0 */6 * * *",
        start_date=pendulum.datetime(2023, 4, 10, tz="Asia/Seoul"),
        catchup=False,
        concurrency=256,
        tags=["example"],
) as dag:
    def fool_fn(**kwargs):
        import time
        time.sleep(600)
        return


    start = EmptyOperator(
        task_id="start",
    )

    for i in range(0, 512):
        start >> PythonOperator(
            task_id=f"fool_task_{i}",
            python_callable=fool_fn,
            email_on_retry=False,
            email_on_failure=False,
        )
