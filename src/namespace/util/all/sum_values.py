import os
import pandas as pd


#file_path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/pipelines/google_daily/data/joined/ad_report_w_campaign_stats.csv"
#file_path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/pipelines/google_daily/data/mutated/ad_report_addHashCols.csv"
#file_path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/pipelines/google_daily/data/joined/ad_report_w_campaign_stats.csv"

# file_path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/cross_pipelines/inuvo_google/data/output/inuvo_google_merged2.csv")
# file_path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/pipelines/google_daily/data/output/google_daily.csv"

file_path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/src/cross_pipelines/inuvo_google/data/output/inuvo_google_merged2.csv"


DT_COL_NAME = "date"

'''
'''
def sum_values(df, col_names, date_list=None):
    # Convert the specified columns to datetime if they're not already
    df[DT_COL_NAME] = pd.to_datetime(df[DT_COL_NAME])

    # Filter DataFrame based on the provided date list
    if date_list:
        df = df[df[DT_COL_NAME].isin(date_list)]

    # Initialize an empty DataFrame to store the result
    result_df = pd.DataFrame({DT_COL_NAME: df[DT_COL_NAME].unique()})

    # Sum each specified column
    for col_name in col_names:
        try:
            result_df[col_name] = df.groupby(DT_COL_NAME)[col_name].sum().values
        except KeyError:
            print(f"Error: The column '{col_name}' does not exist in the DataFrame.")

    return result_df



if __name__ == "__main__":
    cols_to_sum = ["g_impressions"]
    date_li = ["2023-10-20"]
    df = pd.read_csv(file_path)

    result_df = sum_values(df, cols_to_sum, date_li)

    if result_df is not None:
        print(result_df)