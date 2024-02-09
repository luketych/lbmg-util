import psycopg2
import csv

# Database connection details
dbname = 'postgres'
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'

# CSV file details
csv_file = './pipelines/google_daily/data/mutated/ad_stats_campaign_stats_ad_history_cleaned.csv'
table_name = 'ad_stats_campaign_stats_ad_history'



# Connect to the PostgreSQL database
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()

# Create the table schema based on the CSV file columns
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    columns = [f'"{header}" TEXT' for header in headers]  # Assuming all columns are of type TEXT
    
    # Create the table
    create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({", ".join(columns)});'
    cur.execute(create_table_query)

# Import the data from the CSV file
with open(csv_file, 'r') as f:
    cur.copy_from(f, table_name, sep=',', null='')

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()

print(f"Data from {csv_file} imported to the {table_name} table successfully.")
