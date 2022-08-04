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



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>

</details>


### Built With

Tech Stack used in this project

-   [PostgreSQL](https://dev.PostgreSQL.com/doc/)
-   [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/)
-   [dbt](https://docs.getdbt.com/)
-   [Redash](https://redash.io/help/)

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

Make sure you have docker installed on local machine.

-   Docker
-   Docker Compose

### Installation

1. Clone the repo
    ```sh
    git clone https://github.com/Amulah-98/data-warehouse.git
    ```
2. Navigate to the folder

    ```sh
    cd traffic-flow-ELT
    ```

3. Build an airflow image

    ```sh
    docker build . --tag extending_airflow:latest
    ```

4. Run the following command once for first time initialization

    ```sh
     docker-compose up airflow-init
    ```

5. Run
    ```sh
     docker-compose up
    ```
6. Open Airflow web browser
    ```JS
    Navigate to `http://localhost:8000/` on the browser
    activate and trigger load_dag
    activate and trigger transform_dag
    ```



<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

-   [10 Academy](https://www.10academy.org/)
