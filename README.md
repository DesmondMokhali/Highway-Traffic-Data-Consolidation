# Highway-Traffic-Data-Consolidation
Building ETL Data Pipelines with BashOperator using Apache Airflow


## Objectives
In this assignment, I'm going to develop an Apache Airflow DAG that will:

- Extract data from a csv file
- Extract data from a tsv file
- Extract data from a fixed-width file
- Transform the data
- Load the transformed data into the staging area

# 1. Set up the lab environment
1. Start Apache Airflow.  
 ` Open Apache Airflow in IDE `

2. Open a terminal and create a directory structure for the staging area as follows:  
/home/project/airflow/dags/finalassignment/staging.  
`sudo mkdir -p /home/project/airflow/dags/assignment/staging`

3. Execute the following commands to give appropriate permission to the directories.
`sudo chmod -R 777 /home/project/airflow/dags/assignment`

