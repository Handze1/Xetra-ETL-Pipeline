# Xetra-ETL-Pipeline
Xetra stands for Exchange Electronic Trading and it is the trading platform of the Deutsche Börse Group. This dataset is derived near-time on a minute-by-minute basis from Deutsche Börse’s trading system and saved in an AWS S3 bucket available to the public for free.

The ETL Pipeline will extract the Xetra dataset from the AWS S3 source bucket on a scheduled basis, create a report using transformations and load the transformed data to another AWS S3 target bucket.

The pipeline will be written in a way that it can be deployed easily to almost any production environment that can handle containerized applications. The production environment we are going to write the ETL pipeline for consists of a GitHub Code repository, and a DockerHub Image Repository. 
