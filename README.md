# ETL
Overview
This project implements an ETL (Extract, Transform, Load) pipeline to process and analyze data from the IMDb Movies dataset. The pipeline extracts data from a CSV file, performs various data transformations, and loads the cleaned and structured data into a MySQL database. The objective of this project is to demonstrate data engineering skills, including data extraction, transformation, and loading processes.

Project Structure
imdb_movies_data_pipeline.py: The main Python script that contains the ETL pipeline code.
imdb_movies.CSV: The dataset file used for this project.

Prerequisites
Before running the ETL pipeline, ensure you have the following installed:
Python (version 3.x)
MySQL server
MySQL Connector for Python
SQLAlchemy
Pandas library

Installation
To install the required Python libraries, run the following commands:
pip install pandas
pip install mysql-connector-python
pip install SQLAlchemy

Database Setup
Install MySQL: If you don’t have MySQL installed, you can download and install it from MySQL's official website.

Create a Database: Create a new database in MySQL to store the processed data. You can do this using the MySQL command line or any MySQL client.
CREATE DATABASE project_db;

ETL Pipeline Steps
1. Extraction
The data is extracted from the imdb_movies.CSV file using the pandas library.
2. Transformation
Missing values are removed using df.dropna().
Column names are standardized to lowercase and spaces are replaced with underscores.
Date columns are converted to a uniform datetime format.
A new column (profit) is calculated based on revenue and budget_x columns.
3. Loading
The transformed data is loaded into a MySQL database (project_db) using SQLAlchemy.

Running the ETL Pipeline
1) Update Database Credentials: Make sure to update the MySQL connection parameters in the script (imdb_movies_data_pipeline.py) with your own credentials:
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="project_db"
)
2) Run the Python Script:
Open a terminal or command prompt.
Navigate to the directory containing your Python script and the dataset.
Run the script using Python:
python imdb_movies_data_pipeline.py

Validating the Results
After running the script, you can verify that the data has been loaded correctly into the MySQL database.
Use any MySQL client or command line to run a query to check the data:
SELECT * FROM project_db_table LIMIT 5;

