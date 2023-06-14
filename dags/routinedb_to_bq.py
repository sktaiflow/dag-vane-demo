"""
### Description

- ???
"""
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.sktvane.operators.nes import NesOperator


collections = [
    "recommendRoutine",
    "recommendRoutines",
    "recommendRoutineCategory",
    "userRoutine",
]

with DAG(
    dag_id="adot_routinedb_to_bq",
    schedule_interval="0 9 * * *",
    default_args={
        "owner": "안지훈",
        "depends_on_past": False,
        "start_date": datetime(2023, 5, 9),
        "retries": 3,
        "retry_delay": timedelta(minutes=3),
    },
    catchup=False,
    tags=["adot"],
) as dag:
    end = EmptyOperator(task_id="end")
    for c in collections:
        op = NesOperator(
            task_id=f"mongodb_routinedb_{c}_to_bigquery",
            input_nb=f"adot/ipynb/adot_routinedb_to_bq.ipynb",
            parameters={"collection": c, "dt": "{{ ds_nodash }}", "env": "stg"},
        )
        op >> end

dag.doc_md = __doc__
