from pyspark.sql import SparkSession
import pandas as pd
import numpy as np
import os


def create_data_frame_from_csv(spark_instance, csv_file_path):
    # advertiserurl,company,employmenttype_jobstatus,jobdescription,
    # jobid,joblocation_address,jobtitle,postdate,shift,site_name,skills,uniq_id

    # job_title, company, location, description

    file_name = csv_file_path.split("/")[-1]
    data_frame = spark.read.csv(csv_file_path, header=True, inferSchema=True)

    if file_name == "ComputerSystemjobs.csv":
        data_frame = data_frame \
            .drop("Field1") \
            .drop("Field2_Text") \
            .drop("Field3") \
            .drop("Field5") \
            .withColumnRenamed('Title', 'job_title') \
            .withColumnRenamed('Company', 'company') \
            .withColumnRenamed('Location', 'location') \
            .withColumnRenamed('Description', 'description') \

    data_frame = data_frame.dropDuplicates().dropna()
    return data_frame


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
        # "./raw_data/indeed/ProjectManagerJobs.csv",
        # "./raw_data/indeed/SoftwareEngineerJobs.csv",
        # "./raw_data/kaggle/dice_com-job_us_sample.csv",
    ]

    callback_function = lambda file: create_data_frame_from_csv(spark, file)
    data_frames = map(callback_function, csv_paths)

    for derived_dataset in data_frames:
        if derived_dataset is not None:
            derived_dataset.coalesce(1).write.csv("../derived_dataset",
                                                  mode="append",
                                                  header=True,
                                                  quoteAll=True,
                                                  ignoreLeadingWhiteSpace=True,
                                                  ignoreTrailingWhiteSpace=True)

            derived_dataset.printSchema()
            derived_dataset.unpersist()
