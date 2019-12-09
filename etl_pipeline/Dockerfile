FROM jupyter/pyspark-notebook

USER root

WORKDIR /rallyai/spark-etl-pipeline
COPY . .

RUN sudo apt-get update && \
RUN sudo apt-get install libpq-dev python-dev dos2unix vim -y

RUN dos2unix etl_process.py

USER jovyan

EXPOSE 8888

# Uncomment to run via a Jupyter Notebook
# CMD [ "jupyter", "notebook", "--allow-root" ]

CMD [ "/usr/local/spark/bin/spark-submit", "pipeline.py" ]