import pandas as pd
import polars as pl
import pytest
from namespace.util import getTestDir, to_pandas_df


def test_to_pandas_with_polars_df():
    # Test when input is a polars DataFrame
    polars_df = pl.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    result = to_pandas_df(polars_df)
    assert isinstance(result, pd.DataFrame)
    pd.testing.assert_frame_equal(result, polars_df.to_pandas())


def test_to_pandas_with_pandas_df():
    # Test when input is a pandas DataFrame
    pandas_df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    result = to_pandas_df(pandas_df)
    assert isinstance(result, pd.DataFrame)
    pd.testing.assert_frame_equal(result, pandas_df)


def test_to_pandas_with_csv_path():
    # Test when csv path is provided
    test_dir = getTestDir()
    csv_path = f"{test_dir}/resources/test_to_pandas_df/a.csv"
    # with patch("pandas.read_csv") as mock_read_csv:
    #     # Mock the pandas read_csv function
    #     result = to_pandas_df(csv_path=csv_path)
    #     mock_read_csv.assert_called_once_with(csv_path)
    #     assert isinstance(result, pd.DataFrame)
    
    result = to_pandas_df(csv_path=csv_path)
    assert isinstance(result, pd.DataFrame)


def test_invalid_input():
    # Test when input is neither pandas nor polars DataFrame
    with pytest.raises(ValueError):
        to_pandas_df("not_a_dataframe")
