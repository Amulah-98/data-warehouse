# data-warehouse
Scalable data warehouse that will host vehicle trajectory data extracted by analysing footage taken by swarm drones and static roadside cameras
![](image/Flow_Diagram.png)

This project builds a scalable **data warehouse** tech-stack that will help to provide an AI service to a client. The [Data](https://anson.ucdavis.edu/~clarkf/) used for this project is sensor data in csv format. In [Data (ucdavis.edu)](https://anson.ucdavis.edu/~clarkf/) you can find parquet data, and or sensor data in CSV. **ELT pipeline** that extracts data from the links in the website, stages them in MYSQL Database, and transforms data using DBT. This whole process is automated using Airflow. 



# ELT Pipeline
## load_data_airflow.py
ELT pipeline builder

1. `create_tables`
	* create tables using MYSQL and automates using airflow
2. `load_tables`
	* Load raw data from CSV Dataframe to  staging tables and automates using airflow

## dbt_airflow.py
Transforms table using sql files and automates using airflow

## Built With

* [MYSQL](https://www.mysql.com/)
* [Apache Airflow](https://airflow.apache.org/)
* [dbt](https://www.getdbt.com/)
* [Redash](https://redash.io/)

# License
[MIT](https://github.com/nebasam/Data-Warehouse-using-MYSQL)
