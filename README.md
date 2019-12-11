# Tech Job Posting Use of Gender-specific Pronouns Analysis

## Motivation

It's common knowledge that a majority of software engineers identify as male. Despite gains in gender diversity across other STEM professions, software engineering remains largely stagnant. There is a myriad of factors influencing this reality.

We're interested in exploring the role the wording of job postings play in potentially discouraging non-male candidates from applying. This project is inspired by Textio.

## Development

**Note**: Due to depeendency issues this project does notrun on Windows. You'll need to resolve depeendency issues manually.

### Installing Dependencies:

We're using [Pipenv as our enviornment manager](https://pipenv.readthedocs.io/en/latest/).

**Install Dependnecies**

`pipenv install`

**Run Notebook**

`pipenv run jupyter notebook`

or

```shell
pipenv shell
jupter notebook
```

**To run the ETL pipeline**

You might need to install Spark as well as PySpark

`pipenv run spark-submit etl_pipeline/pipeline.py`

### Data

All data is tored in the `/data` directory. `derived_job_data.csv` is the final CSV file created from the pipeline. 