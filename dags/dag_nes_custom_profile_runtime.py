"""
### DAG Documentation
이 DAG는 NES를 사용하는 예제입니다.
"""
from __future__ import annotations

from textwrap import dedent

import pendulum
from airflow import DAG
from airflow.providers.sktvane.operators.nes import NesOperator

with DAG(
    "dag_nes_custom_profile_runtime",
    default_args={"retries": 2},
    description="DAG with own plugins",
    schedule="*/30 * * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["demo"],
) as dag:

    dag.doc_md = __doc__

    nes_task = NesOperator(
        task_id="NES_Custom_Task",
        input_nb="https://github.com/sktaiflow/notebooks/blob/master/test/sample_notebook.ipynb",
        runtime="ye-k8s-custom",
        profile="x1112436",
    )
    nes_task.doc_md = dedent(
        """\
    #### NES task
    NES를 활용한 task 예제
    """
    )

    dag.doc_md = __doc__

    nes_local_task = NesOperator(
        task_id="NES_Local_Task",
        input_nb="sample_notebook.ipynb",
        runtime="ye-k8s-custom",
        profile="x1112436",
    )
    nes_local_task.doc_md = dedent(
        """\
    #### NES Local task
    로컬에 있는 노트북 파일 실행 예제
    """
    )
