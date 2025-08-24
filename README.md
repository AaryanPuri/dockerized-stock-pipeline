# 📊 Dockerized Stock Data Pipeline with Airflow

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Pipeline Workflow](#pipeline-workflow)

---

## About the Project
A **Dockerized Data Pipeline** built with **Apache Airflow** and **PostgreSQL**, designed to fetch stock market data from the **Alpha Vantage API** on a scheduled basis, process it, and store it in a structured database table. The project demonstrates the use of containerized orchestration and ETL workflows.

---

## Features
1. **Automated Data Fetching** – retrieves stock market JSON data hourly via Airflow DAG.  
2. **Data Processing & Storage** – parses the API response and updates PostgreSQL.  
3. **Error Handling** – retries on failure and gracefully handles missing data.  
4. **Dockerized Deployment** – one command (`docker-compose up`) runs the entire pipeline.  
5. **Environment Config** – secrets and configs managed via `.env` (with `example.env` provided).  

---

## Tech Stack
1. **Python 3.7+** – Core language  
2. **Apache Airflow** – Workflow orchestration  
3. **PostgreSQL** – Database for persistent storage  
4. **Docker & Docker Compose** – Containerization and orchestration  
5. **Alpha Vantage API** – Free stock market API (JSON)  
6. **Libraries** – `requests`, `psycopg2-binary`

---

## Installation

### 1. Prerequisites
- Docker Desktop installed and running  
- Git installed  
- Alpha Vantage API key  

### 2. Clone Repository
```bash
git clone https://github.com/AaryanPuri/dockerized-stock-pipeline.git
cd dockerized-stock-pipeline
```

### 3. Configure Environment
Copy the example environment file: `cp example.env .env`
Update .env with your values

### 4. Run Pipeline
`docker-compose up --build`
Airflow UI → `http://localhost:8080`
Login → admin / admin
PostgreSQL → running on localhost:5432

## Pipeline Workflow
1. Airflow Scheduler triggers the DAG (stock_pipeline) every hour.
2. Fetch Task calls fetch_data.py: Retrieves latest stock data (price, volume, timestamp) from Alpha Vantage API & parses JSON and validates response.
3 Database Task inserts data into stock_data table in PostgreSQL. Table is created automatically if it doesn’t exist.
4. Error Handling ensures failures are retried with logging.
