import pandas as pd
import polars as pl


def is_pandas_or_polars(df):
    if isinstance(df, pd.DataFrame):
        return "pandas"
    elif isinstance(df, pl.DataFrame):
        return "polars"
    else:
        return None