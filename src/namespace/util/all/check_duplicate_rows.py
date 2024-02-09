import pandas as pd

def check_duplicate_rows(path_to_csv, key_columns):
    df = pd.read_csv(path_to_csv)
    
    num_lines = len(df)
    print("Number of lines of data: {}".format(num_lines))
    
    # Check if key columns are present in the DataFrame
    missing_columns = [col for col in key_columns if col not in df.columns]
    
    if missing_columns:
        print("Error: The following key columns are not present in the DataFrame: {}".format(missing_columns))
        return
    
    # Check for duplicates based on the specified key columns
    duplicates = df[df.duplicated(subset=key_columns, keep=False)]
    
    if duplicates.empty:
        print("No duplicate rows found.")
    else:
        print("Duplicate rows found:")
        print(duplicates)



# EXAMPLES

# Specify the columns to use as keys for checking duplicates
# key_columns = [
#   'ad_id','date','clicks','conversion','conversion_rate','cost_per_1000_reached','cost_per_conversion','cost_per_result','cost_per_total_purchase','cpm','ctr','impressions','real_time_conversion','real_time_result','spend','video_play_actions'
# ]

# file_path = "/Users/luketych/Dev/_Projects/_lightboxmediaGroup/poetry/data/tiktok/mirrored/segments/s2__mutateData/split2__ad_report_daily/a__addHashCol/lbmg_tiktok_ads.ad_report_daily.csv"

# check_duplicate_rows(file_path, key_columns)