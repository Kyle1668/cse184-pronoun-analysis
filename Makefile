test_flags = --verbose --disable-pytest-warnings
pipeline_file = .\etl_pipeline\pipeline.py

test:
	pipenv run pytest .\etl_pipeline\ $(test_flags)

format:


pipeline:
	pipenv run spark-submit $(pipeline_file)