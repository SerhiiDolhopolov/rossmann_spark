<!-- omit in toc -->
## Languages
[![python](https://img.shields.io/badge/python-3.11-d6123c?color=white&labelColor=d6123c&logo=python&logoColor=white)](https://www.python.org/)

<!-- omit in toc -->
## Frameworks
[![pandas](https://img.shields.io/badge/pandas-2.2.3-d6123c?color=white&labelColor=d6123c&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![minio](https://img.shields.io/badge/minio-7.2.15-d6123c?color=white&labelColor=d6123c&logo=minio&logoColor=white)](https://min.io/)
[![matplotlib](https://img.shields.io/badge/matplotlib-3.10.3-d6123c?color=white&labelColor=d6123c&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![seaborn](https://img.shields.io/badge/seaborn-0.13.2-d6123c?color=white&labelColor=d6123c&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)
[![pyspark](https://img.shields.io/badge/pyspark-4.0.0-d6123c?color=white&labelColor=d6123c&logo=apachespark&logoColor=white)](https://spark.apache.org/docs/latest/api/python/index.html)

<!-- omit in toc -->
## Services
[![docker](https://img.shields.io/badge/docker-d6123c?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![spark](https://img.shields.io/badge/spark-d6123c?style=for-the-badge&logo=apachespark&logoColor=white)](https://spark.apache.org/)

<!-- omit in toc -->
## Table of Contents
- [Introduction](#introduction)
- [Project Workflow](#project-workflow)
- [Docker Containers](#docker-containers)
- [Getting Started](#getting-started)

## Introduction
🟢 **This is part 7 of 7 Docker sections in the 🔴 [Supermarket Simulation Project](https://github.com/SerhiiDolhopolov/rossmann_services).**

🔵 [**<- Preview the part with Airflow.**](https://github.com/SerhiiDolhopolov/rossmann_airflow)

## Project Workflow
This section contains an example of working with large archived dataframes via [Spark](https://spark.apache.org/). 

## Docker Containers
**This Docker section includes:**
  - **Spark master**
    - 🌐 Web interface:
      - [localhost:1701](http://localhost:1701)
  - **Two Spark workers**
  - **Jupyter Lab**
    - 🌐 Web interface:
      - [localhost:8888](http://localhost:8888)

## Getting Started
**To start:**
1. Complete all steps in the [main part](https://github.com/SerhiiDolhopolov/rossmann_services).
2. Run the services:
```bash
docker compose up --build
```
3. Open [localhost:8888](http://localhost:8888)