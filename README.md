Big_data_RSNA_Boneage
This repository provides a robust Big Data pipeline for processing and analyzing the RSNA Pediatric Bone Age Dataset. By leveraging distributed computing frameworks, it streamlines the handling of thousands of pediatric hand radiographs to perform large-scale data cleaning, statistical analysis, and machine learning.


Overview


The project is designed to handle high-volume medical imaging metadata and model outputs using a hybrid approach of Apache Spark for high-speed processing and Apache Hive for structured querying and reporting.
Key Features

Scalable Data Cleaning: Automates the cleaning of raw bone age data using PySpark.

Complex Aggregations: Generates advanced statistics such as average bone age by gender and age-group distribution.

Big Data Analytics: Features dedicated Hive scripts for data warehousing and SQL-like analysis.

ML Integration: Includes a machine learning framework specifically tailored for predicting bone age from processed datasets.

Tech Stack & Languages
Languages
Python: The primary language for data processing scripts and machine learning models.
HQL (Hive Query Language): Used for managing and querying large datasets within the Hive data warehouse.
Big Data Frameworks
Apache Spark (PySpark): Utilized for distributed data transformations and the execution of high-performance analytics.
Apache Hive: Employed for data warehousing, allowing for structured analysis of bone age trends.
Machine Learning & Data Tools
Scikit-learn / MLlib: Powers the predictive modeling components.
Hadoop HDFS: The underlying storage layer for managing large CSV outputs and raw input data.

Repository Structure
PySpark.py: Main script for distributed data cleaning and feature engineering.
Hive.txt: Collection of Hive queries used to create tables and generate analytical reports.
ML Code File: Machine learning implementation for bone age prediction.
/output: Contains results from Spark and Hive jobs, including:
avg_boneage_by_gender
age_group_count
cleaned_boneage_data
