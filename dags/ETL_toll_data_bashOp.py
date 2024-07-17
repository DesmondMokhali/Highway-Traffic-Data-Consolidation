# Import the necessary libraries
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# Define the default arguments
default_args = {
    'owner': 'donchucks', 
    'start_date': days_ago(0),  # today
    'email': ['mokhalibofihla27@gmail.com'],  
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Assignment',
    schedule_interval=timedelta(days=1),
)

# Define the unzip_data task
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xzf /home/donchucks/airflow/dags/assignment/tolldata.tgz -C /home/donchucks/airflow/dags/assignment',
    dag=dag,
)

# Define the extract_data_from_csv task
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command="cut -d',' -f1,2,3,4 /home/donchucks/airflow/dags/assignment/vehicle-data.csv > /home/donchucks/airflow/dags/assignment/csv_data.csv",
    dag=dag,
)

# Define the extract_data_from_tsv task
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command="cut -f5,6,7 /home/donchucks/airflow/dags/assignment/tollplaza-data.tsv | tr '\t' ',' > /home/donchucks/airflow/dags/assignment/tsv_data.csv",
    dag=dag,
)

# Define the extract_data_from_fixed_width task
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command="awk '{print substr($0, 10, 3) \",\" substr($0, 20, 3)}' /home/donchucks/airflow/dags/assignment/payment-data.txt > /home/donchucks/airflow/dags/assignment/fixed_width_data.csv",
    dag=dag,
)

# Define the consolidate_data task
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command="paste -d',' /home/donchucks/airflow/dags/assignment/csv_data.csv /home/donchucks/airflow/dags/assignment/tsv_data.csv /home/donchucks/airflow/dags/assignment/fixed_width_data.csv > /home/donchucks/airflow/dags/assignment/extracted_data.csv",
    dag=dag,
)

# Define the transform_data task
transform_data = BashOperator(
    task_id='transform_data',
    bash_command="awk 'BEGIN {FS=OFS=\",\"} {print $1, $2, $3, toupper($4), $5, $6, $7, $8, $9}' /home/donchucks/airflow/dags/assignment/extracted_data.csv > /home/donchucks/airflow/dags/assignment/transformed_data.csv",
    dag=dag,
)

# Set the task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data
