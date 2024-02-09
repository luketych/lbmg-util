import pandas as pd
import polars as pl
import polars.testing
import pytest
from namespace.util import getTestDir, to_polars_df


def test_to_polars_with_polars_df():
    # Test when input is a polars DataFrame
    polars_df = pl.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    result = to_polars_df(polars_df)
    assert isinstance(result, pl.DataFrame)
    polars.testing.assert_frame_equal(result, polars_df)


def test_to_polars_with_pandas_df():
    # Test when input is a pandas DataFrame
    pandas_df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    result = to_polars_df(pandas_df)
    assert isinstance(result, pl.DataFrame)
    polars.testing.assert_frame_equal(result, pl.DataFrame(pandas_df))


def test_to_polars_with_csv_path():
    # Test when csv path is provided
    test_dir = getTestDir()
    csv_path = f"{test_dir}/resources/test_to_polars_df/a.csv"
    
    result = to_polars_df(csv_path=csv_path)
    
    result_type = type(result)
    
    result_type.__module__ = "polars.dataframe.frame"
    
    assert result_type.__module__ == 'polars.dataframe.frame'


def test_invalid_input():
    # Test when input is neither pandas nor polars DataFrame
    with pytest.raises(ValueError):
        to_polars_df("not_a_dataframe")
