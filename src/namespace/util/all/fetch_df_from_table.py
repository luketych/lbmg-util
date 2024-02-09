import pandas as pd
from sqlalchemy import create_engine


def fetch_df_from_table(conn_str, table_name):
    # Create an SQLAlchemy Engine object
    engine = create_engine(conn_str)

    # Query to fetch data from the inuvo_daily table
    query = f"SELECT * FROM {table_name};"

    # Fetch data using pd.read_sql() with the SQLAlchemy Engine
    df = pd.read_sql(query, engine)
    
    return df