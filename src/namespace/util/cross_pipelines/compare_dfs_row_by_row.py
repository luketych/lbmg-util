import pandas as pd
import polars as pl
from datetime import datetime


def change_column_names_to_lowercase(df):
    new_columns = {col: col.lower() for col in df.columns}
    return df.rename(columns=new_columns)


def get_dataframe_columns(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input is not a DataFrame.")
    return df.columns.tolist()


def compare_dfs_row_by_row(df1, df2, hashCol1Name='hash', hashCol2Name='hash'):
    if isinstance(df1, pl.DataFrame):
        df1 = df1.to_pandas()
    if isinstance(df2, pl.DataFrame):
        df2 = df2.to_pandas()

    _df1 = change_column_names_to_lowercase(df1)
    _df2 = change_column_names_to_lowercase(df2)

    # Sort both dataframes by the 'hash' column
    _df1.sort_values(by=hashCol1Name, inplace=True)
    _df2.sort_values(by=hashCol2Name, inplace=True)

    df1_cols = set(get_dataframe_columns(_df1))
    df2_cols = set(get_dataframe_columns(_df2))

    if df1_cols != df2_cols:
        print(f"Columns in DataFrame 1 but not in DataFrame 2: {df1_cols - df2_cols}")
        print(f"Columns in DataFrame 2 but not in DataFrame 1: {df2_cols - df1_cols}")
        return False

    # Make sure the dataframes have the same shape
    if _df1.shape != _df2.shape:
        print("Dataframes have different shapes.")
        return False
    
    # Iterate through each row and compare them
    for i in range(len(_df1)):
        row1 = _df1.iloc[i]
        row2 = _df2.iloc[i]

        # Compare the values of each column in the row
        for col in df1_cols:
            val1 = row1[col]
            val2 = row2[col]


            # Check for NaN values
            if pd.isna(val1) and pd.isna(val2):
                continue
            if pd.isna(val1) or pd.isna(val2):
                print(f"NaN value in row {i}, column {col}")
                return False

            # Compare non-NaN values with type conversion
            if val1 != val2:
                # Convert numeric types to float for comparison
                if pd.api.types.is_numeric_dtype(row1[col]) and pd.api.types.is_numeric_dtype(row2[col]):
                    try:
                        val1 = float(val1)
                    except ValueError:
                        pass

                    try:
                        val2 = float(val2)
                    except ValueError:
                        pass

                    # Continue with the comparison

                else:
                    # check to make sure it's a valid date format before attempting pd.api.types.is_datetime64_any_dtype()
                    try:
                        if isinstance(row1[col], str):
                            # Attempt to parse the date
                            parsed_date = datetime.strptime(row1[col], "%Y-%m-%d")
                            print("Parsed date:", parsed_date)

                            # Convert datetime types to pandas.Timestamp for comparison
                            if pd.api.types.is_datetime64_any_dtype(row1[col]) and pd.api.types.is_datetime64_any_dtype(row2[col]):
                                try:
                                    val1 = pd.Timestamp(val1)
                                except ValueError:
                                    pass

                                try:
                                    val2 = pd.Timestamp(val2)
                                except ValueError:
                                    pass

                                # If types are not compatible, return False
                                else:
                                    return False

                                if val1 != val2:
                                    print(f"Value mismatch in row {i}, column {col}: {val1} (DF1) vs. {val2} (DF2)")

                    except ValueError as e:
                        # print("Error parsing date:", e)
                        pass


    return True