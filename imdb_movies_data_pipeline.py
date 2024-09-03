#code

!"{sys.executable}" -m pip install pandas

import sys
!"{sys.executable}" -m pip install mysql-connector-python

import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

df=pd.read_csv('C:/Users/HEMA SREE/imdb_movies.CSV')   # Load the dataset

print(df.head)  # Preview the first few rows
print(df.info())  # Get summary of the dataset
print(df.describe())   # Get statistical summary
df = df.dropna()  # Example: Handling missing values

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert date column to datetime format if necessary
df['date_x'] = pd.to_datetime(df['date_x'])
df['profit']= df['revenue']-df['budget_x']
print(df)

# Establish a connection to the MySQL server
#we can use this way or use SQLAlchemy as below
#connection = mysql.connector.connect(
    #host="localhost",
    #user="root",
    #password="Hemasree10",  # replace with your actual root password
    #database="project_db"  # replace with your actual database name
#)
# Create a cursor object
#cursor = connection.cursor()

# Execute a SQL query
#cursor.execute("SELECT * FROM project_db_table")

# Fetch all the rows from the executed query
#results = cursor.fetchall()

# Print the fetched data
#for row in results:
    #print(row)

# Close the cursor and connection
#cursor.close()
#connection.close()

pip install SQLAlchemy

# Create SQLAlchemy engine
engine = create_engine('mysql+mysqlconnector://root:Hemasree10@localhost/project_db')

#to write the contents of a pandas DataFrame (df) to a SQL table in a connected database.
df.to_sql('project_db_table', con=engine, if_exists='replace', index=False)

# Use the engine in pandas read_sql function
df_db = pd.read_sql('SELECT * FROM project_db_table', con=engine)

# Display the DataFrame
print(df_db)
