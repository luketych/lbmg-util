import os
import csv


def extract_rows_by_camp_id(input_file, output_file, camp_id):
    extracted_rows = []
    
    with open(input_file, 'r') as input_csv:
        reader = csv.DictReader(input_csv)
        for row in reader:
            if row.get('camp_id') == camp_id:
                extracted_rows.append(row)

    fieldnames = extracted_rows[0].keys() if extracted_rows else []
    
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(output_file, 'w', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(extracted_rows)

    print(f"New CSV file with rows for camp_id '{camp_id}' created as '{output_file}'.")

  
  

camp_id = '227940'

# extract_rows_by_camp_id('./pipelines/google_daily/mutated_data/ad_history_with_camp_id.csv', './pipelines/google_daily/subset_data/ad_history_with_camp_id.csv', camp_id)

extract_rows_by_camp_id('./pipelines/google_daily/data/download/ad_stats.csv', './pipelines/google_daily/subset_data/ad_stats.csv', camp_id)
extract_rows_by_camp_id('./pipelines/google_daily/data/download/campaign_stats.csv', './pipelines/google_daily/subset_data/campaign_stats.csv', camp_id)