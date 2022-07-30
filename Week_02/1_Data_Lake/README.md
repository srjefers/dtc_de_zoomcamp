# Data Lake

## What is a Data Lake?
Is a central repository that holds big data from many resources, data can be structured, semistructured or unstructured.

Stores, secured and protects data at unlimited scale, connects data with analytics and machine learning tools.

The idea is to ingest data as soon as posible and make it aviable to DS and DA.

## Data Lake vs Data Warehouse
### Data Lake
* **Raw**: Data lakes contain unstructured, semi structured and structured data with minimal processing. It can be used to contain unconventional data such as log and sensor data.
* **Large**: Data lakes contain vast amounts of data in the order of petabytes. Since the data can be in any form or size, large amounts of unstructured data can be stored indefinitely and can be transformed when in use only.
* **Undefined**: Data in data lakes can be used for a wide variety of applications, such as ML, Streaming analytics, and AI.
### Data Warehouse
* **Refined**: Data Warehouses contain highly structured daa that is cleaned, pre-processed and refined. This data is stored for very specific use cases such as BI.

* **Smaller**: Data Warehouses contains less data in the order of terabytes. In order to maintain data cleanliness and health of the warehouse. Data must be processed before ingestion and periodic purging of data is necessary.

* **Relational**: Data Warehouses contain historic and relational data, such as transaction systems, operations, etc.

## How did it start? 
* Companies realized the value of data
* Store and access data quichly
* Cannot always define structure of data
* Usefulness of data being realized later in the project lifecycle.
* Increase in data scientists
* R&D on data products
* Need for Cheap storage of Big data 

## ETL vs ELT
* Export Transform and Load vs Export Load and Transform
* ETL is mainly used for a small amount of data whereas ETL is used for large amounts of data.
* ELT provides data lake support (Schema on read)

## Gotca of Data Lake
* Converting into Data Swamp
* No versioning
* Incompatible schemas for same data without versioning
* No metadata associated
* Joins not possible

## Cloud provider Data Lake
* GCP - Cloud Storage
* AWS - S3
* Azure - Azure BLOB
