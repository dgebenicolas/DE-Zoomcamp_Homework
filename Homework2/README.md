# Green Taxi ETL Pipeline

## Overview
This project constructs an ETL (Extract, Transform, Load) pipeline focused on processing the Green Taxi dataset from New York City's Taxi & Limousine Commission (NYC TLC). The data covers trips made in the final quarter of 2020 (October, November, December).

## Pipeline Construction
The pipeline, named `green_taxi_etl`, was built using a combination of Pandas for data manipulation and PyArrow for data storage, alongside SQL for database interactions. The process involves loading the data, applying necessary transformations, and finally writing the processed data to both a PostgreSQL database and Google Cloud Storage in Parquet format.

## Data Source
The dataset was obtained from the [DataTalksClub NYC TLC Data Releases](https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/green/download), specifically targeting green taxi trip records.

## Key Steps
1. **Data Loading**: Data for the targeted months was dynamically loaded using Pandas, leveraging a loop to concatenate data for each month efficiently.
2. **Transformation**:
   - Removal of records with zero passenger count or trip distance.
   - Generation of a new column for pickup dates.
   - Standardization of column names to snake case.
3. **Assertions**: Ensured data quality by asserting conditions on `vendor_id`, `passenger_count`, and `trip_distance`.
4. **Data Storage**:
   - Utilized SQL to store the processed data in a PostgreSQL table within the `mage` schema.
   - Exported data to Google Cloud Storage as Parquet files, partitioned by pickup date.
5. **Scheduling**: Configured the pipeline to execute daily at 5 AM UTC, ensuring up-to-date data availability.

## Objective
The primary goal of this project was to demonstrate the capability to automate the processing and management of large datasets through a reliable ETL pipeline, facilitating easy access and analysis of cleaned taxi trip data.

