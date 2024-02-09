import csv
import os

# from .filter_for_cols import filter_for_cols
# from .read_csv import read_csv
# from .write_data_to_csv import write_data_to_csv



def csv_extract_rows_with_date(data, given_date):
    result_rows = [row for row in data if row['date'] == given_date]
    return result_rows
 


# EXAMPLE USAGE

# data = read_csv('./pipelines/google_daily/downloaded_data/ad_stats.csv')
# res1 = csv_extract_rows_with_date(data, '2023-07-02')
# res2 = filter_for_cols(res1, ['ad_group_id', 'ad_id', 'campaign_id', 'clicks', 'conversions', 'cost_micros', 'date', 'impressions', 'interactions'])
                           
# write_data_to_csv(res2, './pipelines/google_daily/test_data', 'filtered_ad_stats.csv')