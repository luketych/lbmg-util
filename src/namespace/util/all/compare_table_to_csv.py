import os
import pandas as pd
import polars as pl
import sys

from .compare_dataframes_row_by_row import compare_dataframes_row_by_row
from .print_color import print_color


def compare_table_to_csv(conn, table_name, csv_file, hashCol1Name, hashCol2Name):
    query = f"COPY {table_name} TO STDOUT WITH (FORMAT csv, HEADER true);"
    with open(f"/tmp/{table_name}.csv", "w") as f:
        with conn.cursor() as cursor:
            cursor.copy_expert(query, f)

    df_database = pl.read_csv(f"/tmp/{table_name}.csv")
    df_csv = pl.read_csv(csv_file)
    
    
    # temp
    # df_database.write_csv("./pipelines/bing-daily/data/test/database.csv")
    # df_csv.write_csv("./pipelines/bing-daily/data/test/csv.csv")
    
    
     
    is_data_equal = compare_dataframes_row_by_row(df_database, df_csv, hashCol1Name, hashCol2Name)

    if is_data_equal:
        print("Data in the database matches the supplied CSV file.")
    else:
        print_color("Data in the database does not match the supplied CSV file.", "red")