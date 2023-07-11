# Sample dags for Vane demo

Vane Demo를 위한 Sample Dags
- /dags/dag_nes.py :    NesOperator 샘플 DAG
- /dags/dag_with_plugsin.py :    custom plugins 샘플 DAG
- /plugins :    custom plugins 디렉토리
- /tests :    DAG Test 샘플 디렉토리

## 테스트 수행 가이드
- Pycharm으로 실행시 Settings >> Project Structure 에서 dags, plugins 폴더를 Source Folder로 설정해주셔야합니다.
- pytest, pytest-mock 패키지가 설치되어 있어야 합니다.
- 테스트를 진행하지 않을 DAG의 경우 tests/.dagtestignore 파일에 DAG 파일명을 추가해주세요.