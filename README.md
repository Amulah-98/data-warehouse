# data-warehouse
Scalable data warehouse that will host vehicle trajectory data extracted by analysing footage taken by swarm drones and static roadside cameras



![Flow_Diagram](https://user-images.githubusercontent.com/55177259/180666757-6a75971c-4545-49fc-a7a4-930f049fd11f.png)



### ELT Pipeline
### load_data_airflow.py
ELT pipeline builder

1. `create_tables`
	* create tables using Postgres and automates using airflow
2. `load_tables`
	* Load raw data from CSV Dataframe to  staging tables and automates using airflow

### dbt_airflow.py
Transforms table using sql files and automates using airflow

## Built With

* [MYSQL](https://www.postgres.com/)
* [Apache Airflow](https://airflow.apache.org/)
* [dbt](https://www.getdbt.com/)
* [Redash](https://redash.io/)

