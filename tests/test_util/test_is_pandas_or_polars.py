import pandas as pd
import polars as pl
from namespace.util import is_pandas_or_polars


def test_is_pandas_dataframe():
    # Test when input is a pandas DataFrame
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    result = is_pandas_or_polars(df)
    assert result == "pandas"


def test_is_polars_dataframe():
    # Test when input is a polars DataFrame
    df = pl.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    result = is_pandas_or_polars(df)
    assert result == "polars"


def test_invalid_input():
    # Test when input is neither pandas nor polars DataFrame
    result = is_pandas_or_polars("not_a_dataframe")
    assert result is None
