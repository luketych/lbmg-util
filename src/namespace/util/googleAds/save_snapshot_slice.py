# from namespace.util.index import csv_extract_rows_with_date, filter_for_cols#, write_data_to_csv
from .csv_extract_rows_with_date import csv_extract_rows_with_date
from .filter_for_cols import filter_for_cols
from ..csv.write_data_to_csv import write_data_to_csv


''' @date_string: 'ie 2023-07-02' '''
def save_snapshot_slice(data, output_filename, date_string, filters=[]):
    filtered_data = csv_extract_rows_with_date(data, date_string)
    
    filtered_data = filter_for_cols(filtered_data, filters)
    
    write_data_to_csv(filtered_data, './pipelines/google_daily/data/test/t1_ad_stats_and_ad_history', output_filename)