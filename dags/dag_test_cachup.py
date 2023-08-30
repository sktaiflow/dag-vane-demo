"""
### DAG Documentation
이 DAG는 catchup 기능을 테스트 하는 예제입니다.
"""
from __future__ import annotations

from textwrap import dedent

import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.sktvane.operators.nes import NesOperator


with DAG(
    "dag_test_catchup",
    default_args={"retries": 2},
    description="DAG with adot_user",
    schedule="10 8 * * *",
    start_date=pendulum.datetime(2023, 7, 1, tz=pendulum.timezone('Asia/Seoul')),
    catchup=True,
    tags=["adot_user"],
) as dag:

    dag.doc_md = __doc__

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

    dag.doc_md = __doc__

    nes_local_task = NesOperator(
        task_id="NES_Local_Task",
        input_nb="sample_notebook.ipynb",
    )
    nes_local_task.doc_md = dedent(
        """\
    #### NES Local task
    로컬에 있는 노트북 파일 실행 예제
    """
    )

    def check_dags_folder(**kwargs):
        from airflow.configuration import conf
        dags_folder = conf.get("core", "dags_folder")

        print(f"DAGS FOLDER: {dags_folder}")


    dir_check_task = PythonOperator(
        task_id="check_dags_folder",
        python_callable=check_dags_folder,
    )
