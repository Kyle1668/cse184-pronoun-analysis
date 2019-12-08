test_flags = --verbose --disable-pytest-warnings
pipeline_file = .\etl_pipeline\pipeline.py

unit-tests:
	pytest .\etl_pipeline\ $(test_flags)

format:
	

etl-pipeline:
	pipenv run spark-submit $(pipeline_file)