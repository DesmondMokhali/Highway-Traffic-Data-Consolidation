# Highway Traffic Data Consolidation: An Airflow ETL Pipeline

This project tackles national highway decongestion through data analysis from various toll plazas. Each plaza, managed by different operators, uses unique file formats. My objective is to consolidate this data into a single, usable format.  

![traffic](https://github.com/user-attachments/assets/057d1c7f-bfc4-4471-9e3c-c4bcd7ee5323)

Photo by <a href="https://unsplash.com/@uimartin?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">ui-martin</a> on <a href="https://unsplash.com/photos/a-busy-city-street-filled-with-lots-of-traffic-SuKAltSwdxs?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  


### Objectives  
- Leverage Apache Airflow to construct a Data Extraction, Transformation, and Load (ETL) pipeline.  
- Extract data from CSV, TSV, and fixed-width files.  
- Perform data transformation.  
- Load the transformed data into a staging area.  
  
## 1. Environment Setup 
1. **Terminal:**
- Launch your terminal (Linux or WSL for Windows).  

2. **Staging Area:**    
- Create a directory structure:  
 `sudo mkdir -p /home/project/airflow/dags/finalassignment/staging`  

- Grant appropriate permissions:  
`sudo chmod -R 777 /home/project/airflow/dags/finalassignment`  
  
3. **Data Download:**    
- Download the dataset using curl:  
`sudo curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz -o /home/project/airflow/dags/finalassignment/tolldata.tgz`  

## 2: Building the DAG  
  
1. **ETL_toll_data_bashOp.py:**   
- Create this file in your project directory `nano ETL_toll_data_bashOp.py`.  
- Import necessary libraries.  
  ![Import_libraries](https://github.com/user-attachments/assets/626f5f13-87cc-4d16-9b90-57043c52965e)

2. **DAG Arguments:**  
- Define arguments like start_date and email within the file.  

  ![dag_args](https://github.com/user-attachments/assets/dbfb8886-6c88-4feb-affb-2fb0fb026967)


3. **DAG Definition:**  
- Define the DAG object with a clear description and schedule.  

![dag_definition](https://github.com/user-attachments/assets/4820e025-d7a8-4bc0-b9ed-2e9418e39121)

## 3. Tasks with BashOperator      
  
1. **unzip_data:** 
- Unzip the downloaded data using the `tar` command.  

![unzip_data](https://github.com/user-attachments/assets/85502379-3b6f-4707-b3e5-f2aa1ce5d2d0)


2. **extract_data_from_csv:**
- Extract specific fields from `vehicle-data.csv` and save them as `csv_data.csv`.

![extract_data_from_csv](https://github.com/user-attachments/assets/407b2852-6d01-4d4c-bfc7-de82fcfd2eef)


3. **extract_data_from_tsv:** 
- Extract specific fields from `tollplaza-data.tsv` and save them as `tsv_data.csv`.  

![extract_data_from_tsv](https://github.com/user-attachments/assets/854d621c-415a-453c-84ee-6f568042fef5)


4. **extract_data_from_fixed_width:** 
- Extract specific fields from `payment-data.txt` and save them as `fixed_width_data.csv`.  

![extract_data_from_fixed_width](https://github.com/user-attachments/assets/0687cbdb-4234-4b32-8b81-fac38da3d0c2)

5. **consolidate_data:** 
- Combine data from the extracted CSV files into a single `extracted_data.csv`.  

![consolidate_data](https://github.com/user-attachments/assets/b5d900fb-2914-4554-bb02-5dbbdbbece8f)

6. **transform_data:** 
- Convert the `vehicle_type` field in `extracted_data.csv` to uppercase and save as `transformed_data.csv` in the staging area.  

![transform](https://github.com/user-attachments/assets/e5cb1800-d58a-4fe8-bbcc-5468aa5c1867)

7. **Task Pipeline:** 
- Define the order of task execution based on dependencies.  

![task_pipeline](https://github.com/user-attachments/assets/dfab1d25-e3cb-4cad-84bd-3f336de0a00c)

## 4. DAG Operations
1. **Submit the DAG:**    
- Use the Airflow CLI or Web UI to submit the DAG

![submit_dag](https://github.com/user-attachments/assets/2a4b9421-7cb3-4323-816e-5ca8fb3bc278)

2. **Unpause & Trigger:**
- Unpause and trigger the DAG execution through the CLI or Web UI.

![unpause_trigger_dag](https://github.com/user-attachments/assets/cd470aeb-cb9c-4f30-a17f-af3ea8e28a27)

## 5. DAG Tasks

![dag_tasks](https://github.com/user-attachments/assets/70916da0-865c-4268-abdc-62a147ff764c)


## 6. DAG Runs

![dag_runs](https://github.com/user-attachments/assets/2cf4a297-22ab-407b-9efb-fd02096632df)


![dag_runs_2](https://github.com/user-attachments/assets/f8a9f2d5-cdff-446d-b8cd-8d3ff8bdf434)


## Conclusion
This document has outlined a professional data engineer's approach to building an Apache Airflow DAG for consolidating traffic data from various toll plazas. This exercise served as valuable practice for the skills I acquired during the IBM Data Engineering certificate program. By leveraging BashOperator tasks and data transformation techniques, we can effectively extract, transform, and load the data into a staging area for further analysis. This approach paves the way for streamlined traffic management and potential decongestion strategies on national highways.
