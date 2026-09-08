# Weather Data Pipeline

An end-to-end data engineering project that collects weather data from the Open-Meteo API and processes it using PySpark and Databricks.

## Technologies

* Python
* PySpark
* Databricks
* Delta Lake
* Apache Airflow

## Pipeline

```text
Open-Meteo API
      ↓
   PySpark
      ↓
    Bronze
      ↓
    Silver
      ↓
     Gold
      ↑
  Databricks
      ↑
   Airflow
```

## What the pipeline does

* Collects weather data from the Open-Meteo API
* Stores raw data in the Bronze layer
* Cleans and validates data in the Silver layer
* Creates daily weather statistics in the Gold layer
* Uses Delta Lake for data storage
* Uses Airflow to trigger the Databricks Job

## Data Quality

The pipeline checks for:

* Empty data
* Invalid temperature
* Negative wind speed
* NULL latitude/longitude
* NULL weather code
* NULL timestamp
