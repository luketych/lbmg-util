from typing import Union
import pandas as pd
import polars as pl
from polars import DataFrame as PolarsDataFrame

from .is_pandas_or_polars import is_pandas_or_polars


def to_pandas_df(df: Union[PolarsDataFrame, pl.DataFrame] = None, csv_path: str = None):
    # if already pandas then just return
    if is_pandas_or_polars(df) == "pandas":
        return df
      
    # if polars then convert to pandas
    elif is_pandas_or_polars(df) == "polars":
        ret_df = df.to_pandas()
      
        return ret_df
      
    # if csv path then read csv into pandas
    elif csv_path:
        df = pd.read_csv(csv_path)
      
        return df
      
    else:
        raise ValueError("Input must be either a pandas or polars DataFrame or a csv path")