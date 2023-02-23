# My First Data Project

![GitHub](https://img.shields.io/github/license/bramvdklinkenberg/my_first_data_project?style=flat-square)
![GitHub language count](https://img.shields.io/github/languages/count/bramvdklinkenberg/my_first_data_project?style=flat-square)
![GitHub top language](https://img.shields.io/github/languages/top/bramvdklinkenberg/my_first_data_project?style=flat-square)
[![Flake8 Lint](https://github.com/bramvdklinkenberg/my_first_data_project/actions/workflows/flake8-lint.yml/badge.svg)](https://github.com/bramvdklinkenberg/my_first_data_project/actions/workflows/flake8-lint.yml?label=flask8&style=flat-square)
[![CodeQL Code Analysis](https://github.com/bramvdklinkenberg/my_first_data_project/actions/workflows/codeql-code-analysis.yml/badge.svg)](https://github.com/bramvdklinkenberg/my_first_data_project/actions/workflows/codeql-code-analysis.yml?label=flask8&style=flat-square)


## Introduction

At the end of 2022 I made the decision that I wanted to make a \"career switch\" from being a Cloud Native Engineer to becoming a Data Engineer.
I had made a rough roadmap for myself on how I thought I could make the switch. I first studied for and passed the [DP-900 Azure Data Fundamentals](https://learn.microsoft.com/en-us/certifications/exams/dp-900/) exam and right away started studying for the [DP-203 Azure Data Engineering](https://learn.microsoft.com/en-us/certifications/exams/dp-203) exam. Right away I noticed that my SQL was too rusty and I missed a solid base of knowledge and experience with Python.

After asking for advice and looking around on the internet I decided to do the [Data Engineering with Python](https://app.datacamp.com/learn/career-tracks/data-engineer-with-python) Career Track from Datacamp, but befor I could start that one I first completed the [SQL Fundamentals](https://app.datacamp.com/learn/skill-tracks/sql-fundamentals), [Python Fundamentals](https://app.datacamp.com/learn/skill-tracks/python-fundamentals) and [Python Programming](https://app.datacamp.com/learn/skill-tracks/python-programming) Skill Tracks. All tracks are short videos explaining a subject and then right away putting it to practice with hands-on exercises. I really enjoyed the Datacamp courses and I would recommend them to anyone who wants to learn (more about) SQL, Python and Data Engineering.

Instead of focussing on the DP-203 exam I decided I wanted to first get more hands-on experience with SQL and Python. So, I started working on my first data project and make sure that I use different data sources and data formats to build a portfolio.

This is a data project that focuses on uploading, transforming, and loading data into an Azure PostgreSQL database, making use of Bash, Python, SQL and Github Workflows.

Once I get this nicely up and running I will start working on different setups, using the same data, but using tools like Airflow, Mage, Azure Data Factory, Azure Synapse, Azure Databricks, PySpark etc. This way I can get more hands-on experience with different tools and technologies.

I have also created a "My first data engineering project from scratch" blog post on my website. You can find it [here](https://bramvandenklinkenberg.com/2023/02/22/my-first-data-engineering-project-from-scratch/).

## Prerequisites

Before we can run the pipelines we need to have some requirements in place:

- **An Azure Account**
  - If you don\'t have an Azure Account, you can create a free account by following [these](https://azure.microsoft.com/en-us/free/) instructions.
- **An Azure Storage Account**
  - If you don\'t have an Azure Storage Account, you can create one by following [these](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create) instructions in this.
- **An Azure PostgreSQL database**
  - If you don\'t have an Azure PostgreSQL database (single server), you can create one by following the instructions in this [quickstart guide](https://learn.microsoft.com/en-gb/azure/postgresql/single-server/quickstart-create-server-database-portal).
- **Hygrometer data**
  - You can checkout the format of the [CSV](./data/humidity_livingroom.csv) file I exported from my hygrometer.
- **Weather API**
  - You can [register](https://www.visualcrossing.com/) and get an API key.
- **Github Actions Secrets**
  - You need to create the following secrets in your Github repository:
    - **AZURE_CLIENT_ID**: The client ID of your Azure Service Principal.
    - **AZURE_CLIENT_SECRET**: The client secret of your Azure Service Principal.
    - **AZURE_TENANT_ID**: The tenant ID of your Azure Service Principal.
    - **AZURE_STORAGE_ACCOUNT_NAME**: The name of your Azure Storage Account.
    - **AZURE_POSTGRESQL_HOSTNAME**: The hostname of your Azure PostgreSQL database.
    - **AZURE_POSTGRESQL_ADMIN**: The admin username of your Azure PostgreSQL database.
    - **AZURE_POSTGRESQL_ADMIN_PASSWORD**: The admin password of your Azure PostgreSQL database.
    - **WEATHER_API_KEY**: The API key of your Weather API.

## Project Structure

The project is structured as follows:

- **.github/workflows**: This directory contains the Github Workflows.
  - More information about the specific workflows can be found in the Workflows section.
- **/data**: This directory contains the CSV file with humidity data.
- **/etl**: This directory contains the code for the ETL process. It contains:
  - **\_\_init\_\_.py**: This file initializes the `etl` package and imports the modules from the etl directory.
  - **constants.py**: Contains all the variables used across in the package.
  - **humidity_data_etl_pipeline.py**: Contains the user-defined functions specific to transforming the humidity data.
  - **utils.py**: Contains generic user-defined functions used in the package.
  - **weather_data_etl_pipeline.py**: Contains the user-defined functions specific to transforming the weather data fetched from weather API.
- **/scripts/bash**: This directory contains a Bash script that uploads the CSV file to an Azure storage account.
- **requirements.txt**: This file contains a list of modules and packages that are required by the project.

## Workflows

The project has four workflows[^1]:

1. **codeql-code-analysis.yml**: This workflow runs semantic code analysis against the repository's source code to find security vulnerabilities. 
2. **flake8-lint.yml**: This workflow runs the flake8 linter on the Python code in the /etl directory.
3. **humidity-data-etl-pipeline.yml**: This workflow extracts, transforms, and loads the humidity data from the uploaded CSV file  into the Azure PostgreSQL database. The workflow uses the modules in the `etl` package.
4. **upload-humidity-data.yml**: This workflow executes the Bash script located in the /scripts/bash directory, which uploads the CSV file to an Azure storage account[^2].
5. **weather-data-etl-pipeline.yml**: This workflow fetches weather data from a weather API, transforms the data using the modules in the `etl` package, and loads the data into the same Azure PostgreSQL database as the humidity data.

[^1]: All workflows can be run manually. The only workflow that is triggered automatically is the flake8 lint workflow. This workflow is triggered automatically with a pull request or a push to the main branch.

[^2]: It is not a pipeline that is necessary, because you can also fetch the file locally when you want to adjust the data. In this case I wanted to show I can use Bash and the Azure CLI.
