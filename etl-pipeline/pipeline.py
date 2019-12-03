from pyspark.sql import SparkSession, DataFrame
import pandas as pd
import numpy as np
import os


def create_data_frame_from_csv(spark_instance, csv_file_path):
    """This function creates a daat frame from a CSV file and cleans itself.
       The column names are changed to matched the agreed on schema for analysis.
       Schema: job_title, company, location, description

    Args:
        spark_instance (SparkSession.builder): The spark session to use the df methods from
        csv_file_path (Str): Path to the CSV file

    Returns:
        pyspark.sql.DataFrame: The cleaned pyspark data frame of the CSV file
    """

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
            .withColumnRenamed('Description', 'description')

    elif file_name == "ProjectManagerJobs.csv":
        data_frame = data_frame \
            .drop("Field4") \
            .withColumnRenamed('Field1', 'job_title') \
            .withColumnRenamed('Field2', 'company') \
            .withColumnRenamed('Field3', 'location') \
            .withColumnRenamed('Field6', 'description') \
            .where("location != '-'")

    elif file_name == "SoftwareEngineerJobs.csv":
        data_frame = data_frame \
            .withColumnRenamed('Title', 'job_title') \
            .withColumnRenamed('Company', 'company') \
            .withColumnRenamed('Location', 'location') \
            .withColumnRenamed('Description', 'description')

    elif file_name == "dice_com-job_us_sample.csv":
        data_frame = data_frame \
            .drop("advertiserurl") \
            .drop("employmenttype_jobstatus") \
            .drop("jobid") \
            .drop("postdate") \
            .drop("shift") \
            .drop("site_name") \
            .drop("skills") \
            .drop("uniq_id") \
            .withColumnRenamed('jobtitle', 'job_title') \
            .withColumnRenamed('joblocation_address', 'location') \
            .withColumnRenamed('jobdescription', 'description')

    elif file_name == "monster_com-job_sample.csv":
        data_frame = data_frame \
            .where("country = 'United States of America'") \
            .drop("country") \
            .drop("country_code") \
            .drop("date_added") \
            .drop("has_expired") \
            .drop("job_board") \
            .drop("job_type") \
            .drop("page_url") \
            .drop("salary") \
            .drop("sector") \
            .drop("uniq_id") \
            .withColumnRenamed('organization', 'company') \
            .withColumnRenamed('job_description', 'description') \

    data_frame = data_frame \
        .dropDuplicates() \
        .dropna() \
        .select("job_title", "company", "location", "description")

    return data_frame


def combine_datasets(spark, raw_datasets_paths):
    """This function takes in a list of CSV files and returns the combined data
       frame from their values. Rows with misisng data and duplicates are removed.

    Args:
        spark (SparkSession.builder): The spark session to use the df methods from
        raw_datasets_paths (list[str]): Path to the CSV files

    Returns:
        pyspark.sql.DataFrame: The combined cleaned data frame
    """
    data_frames = [
        create_data_frame_from_csv(spark, file) for file in raw_datasets_paths
    ]

    if (len(data_frames) > 0):
        combined_data_frame = data_frames[0]

        if (combined_data_frame != None):
            for derived_dataset in data_frames:
                combined_data_frame = combined_data_frame.union(derived_dataset)
                derived_dataset.printSchema()
                derived_dataset.unpersist()

        return combined_data_frame.dropDuplicates()

    return None


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
    working_directory_path = os.path.dirname(os.path.realpath(__file__))
    raw_datasets_paths = [
        f"{working_directory_path}/raw_data/indeed/ComputerSystemjobs.csv",
        f"{working_directory_path}/raw_data/indeed/ProjectManagerJobs.csv",
        f"{working_directory_path}/raw_data/indeed/SoftwareEngineerJobs.csv",
        f"{working_directory_path}/raw_data/kaggle/dice_com-job_us_sample.csv",
        f"{working_directory_path}/raw_data/monster/monster_com-job_sample.csv",
    ]

    # Get combined data frame from the distriubted data frames
    combined_data_frame = combine_datasets(spark, raw_datasets_paths)

    # Write the combined data frame to local CSV file for further analysis
    if combine_datasets != None:
        combined_data_frame.coalesce(1).write.csv(
            f"{working_directory_path}/../derived_data",
            mode="append",
            header=True,
            quoteAll=True,
            ignoreLeadingWhiteSpace=True,
            ignoreTrailingWhiteSpace=True)
