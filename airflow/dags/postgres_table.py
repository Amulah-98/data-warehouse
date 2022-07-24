import airflow
from datetime import timedelta
from airflow import DAG
from airflow.models import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

args={'owner': 'airflow'}

default_args = {
    'owner': 'airflow',    
    #'start_date': airflow.utils.dates.days_ago(2),
    # 'end_date': datetime(),
    # 'depends_on_past': False,
    #'email': ['airflow@example.com'],
    #'email_on_failure': False,
    # 'email_on_retry': False,
    # If a task fails, retry it once after waiting
    # at least 5 minutes
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag_psql = DAG(
    dag_id = "postgresoperator_demo",
    default_args=args,
    # schedule_interval='0 0 * * *',
    schedule_interval='@once',	
    dagrun_timeout=timedelta(minutes=60),
    description='use case of psql operator in airflow',
    start_date = airflow.utils.dates.days_ago(1)
)


create_table_sql_query = """ 
            CREATE TABLE  IF NOT EXISTS traffic (
            track_id numeric, 
            type text not null, 
            traveled_d double precision DEFAULT NULL,
            avg_speed double precision DEFAULT NULL, 
            lat double precision DEFAULT NULL, 
            lon double precision DEFAULT NULL, 
            speed double precision DEFAULT NULL,    
            lon_acc double precision DEFAULT NULL, 
            lat_acc double precision DEFAULT NULL, 
            time double precision DEFAULT NULL
            );
"""

##load data
import csv
import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
cur = conn.cursor()
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO users VALUES (%s, %s, %s, %s)",
        row
    )
conn.commit()

##donnecting directly from postgres
conn = pg_connect(
 host='localhost',
 user='postgres', # This is a default value. It may be your username.
 database=pNEUMA,
 # password='<password>', # By default, the password is empty. You can choose to enforce a password.
 # port='5432', # This is a default value and can be omitted


create_table = PostgresOperator(
    sql = create_table_sql_query,
    task_id = "create_table_task",
    postgres_conn_id = "postgres_local",
    dag = dag_psql
    )

load_data = PostgresOperator(
    sql = cur,
    task_id = "insert_data_task",
    postgres_conn_id = "postgres_local",
    dag = dag_psql
    )


create_table >> load_data

    if __name__ == "__main__":
        dag_psql.cli()