# DTC Data Engineering ZoomCamp

## Proposal Architecture on GCP
<p align="center">
    <img width="700" alt="Alacritty Logo" src="https://raw.githubusercontent.com/srjefers/dtc_de_zoomcamp/main/Proposal_Architecture.jpg">
</p>

## Tech Stack
* Goocle Cloud Platform
* Terraform
* Docker
* SQL
* Airflow
* dbt
* Spark
* Kafka

## Week 01
### _Intro and Prerequisites_
* Setting up the Environment
* Google Cloud Account
    1. Docker
    2. Terraform
* Running Postgres in Docker
* Taking a look at the NY Taxi dataset
* SQL refresher
## Week 02
### _Ingestion and Orchestration_
* Data Lake
    1. What is a Data Lake
    2. ETL vs ELT
    3. Using GCS
* Orchestration
    1. What is an Orchestration Pipeline
    2. Data Ingestion
    3. Introducing & Using Airflow
* Demo
    1. Setting up Airflow with Docker
    2. Data Ingestion DAG
        - Extraction
        - Pre-processing (parquet, partitioning)
        - Loading
        - Exploration with Big Query
* Best Practices
## Week 03
### _Data Warehouse_
* What is Data Warehouse?
* BigQuery?
    1. Partitioning and Clustering
    2. With Airflow
    3. Best Practices
## Week 04
### _Analytics Engineering_
* What is dbt and how does it fit the tech stack?
* Using dbt:
    1. Anatomy of a dbt model
    2. Seeds
    3. Jinja, Macros and test
    4. Documentation
    5. Packages
* Build a dashboard in Google Data Studio
## Week 05
### _Batch Processing_
* Spark internals
* Broadcasting
* Partitioning
* Shuffling
* Spark + Airflow
* Apache Flink as alternative
## Week 06
### _Stream Processing_
* Basics of Kafka
* Consumer-Producer
* Kafka Streams
* Kafka Connect
