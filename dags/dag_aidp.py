"""
### DAG Documentation
이 DAG는 NES를 사용하는 예제입니다.
"""
from __future__ import annotations

from textwrap import dedent

import pendulum
from airflow import DAG
from airflow.providers.sktvane.operators.nes import NesOperator
from airflow.providers.sktvane.sensors.gcp import BigqueryPartitionSensor


with DAG(
    "dag_aidp",
    default_args={"retries": 2},
    description="DAG with own plugins",
    # schedule="*/2 * * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["demo"],
) as dag:

    dag.doc_md = __doc__

    sensor = BigqueryPartitionSensor(
        task_id="sense_bq_part",
        project_id="skt-datahub",
        dataset_id="x1112596",
        table_id="ob_roaming_country_copy",
        partition="2023-04-01",
    )
    sensor.doc_md = dedent(
        """\
    #### BigQuery partition sensor
    BigQuery 파티션 센서 예제
    """
    )

    nes_task = NesOperator(
        task_id="NES_Task",
        input_nb="https://github.com/sktaiflow/notebooks/blob/master/test/sample_notebook.ipynb",
    )
    nes_task.doc_md = dedent(
        """\
    #### NES task
    NES를 활용한 task 예제
    """
    )

    sensor >> nes_task
