from pyspark.sql import SparkSession
import pandas as pd
import numpy as np
import os


def create_data_frame_from_csv(spark_instance, csv_file_path):
    try:
        return spark.read.csv(csv_file_path, header=True, inferSchema=True)
    except:
        pass


if __name__ == "__main__":

    # Initialize Spark Configuration
    spark_master = os.environ.get("SPARK_MASTER") if os.environ.get(
        "SPARK_MASTER") is not None else "local[8]"

    spark_app_name = os.environ.get("SPARK_APP_NAME") if os.environ.get(
        "SPARK_APP_NAME") is not None else "gendered_job_posting_analysis"

    spark_max_memory = os.environ.get("SPARK_MEMORY_CAP") if os.environ.get(
        "SPARK_MEMORY_CAP") is not None else "6g"

    spark = SparkSession.builder \
        .master(spark_master) \
        .appName(spark_app_name) \
        .config("spark.driver.memory", spark_max_memory) \
        .getOrCreate()

    # Init new loggers
    log4jLogger = spark._jvm.org.apache.log4j
    log = log4jLogger.LogManager.getLogger(__name__)

    # Create data frames from CSV Files
    csv_paths = [
        "./raw_data/indeed/ComputerSystemjobs.csv",
        "./raw_data/indeed/ProjectManagerJobs.csv",
        "./raw_data/indeed/SoftwareEngineerJobs.csv",
        "./raw_data/kaggle/dice_com-job_us_sample.csv",
    ]

    data_frames = map(lambda file: create_data_frame_from_csv(spark, file), csv_paths)

    for df in data_frames:
        df.printSchema()
