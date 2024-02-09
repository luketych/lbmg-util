from typing import Union
import pandas as pd
import polars as pl
from polars import DataFrame as PolarsDataFrame

from .is_pandas_or_polars import is_pandas_or_polars


def to_polars_df(df: Union[PolarsDataFrame, pd.DataFrame] = None, csv_path: str = None):
    # if already polars then just return
    if is_pandas_or_polars(df) == "polars":
        return df
      
    # if pandas then convert to polars
    elif is_pandas_or_polars(df) == "pandas":
        return pl.from_pandas(df)
      
    # if csv path then read csv into polars
    elif csv_path:
        return pl.read_csv(csv_path)

    else:
        raise ValueError("Input must be either a pandas or polars DataFrame or a csv path")