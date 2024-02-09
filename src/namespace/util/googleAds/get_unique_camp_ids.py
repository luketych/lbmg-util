import csv

def extract_unique_camp_ids(csv_file):
    camp_ids = set()  # Initialize an empty set to store unique camp_ids

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            camp_id = row.get('camp_id')  # Assuming 'camp_id' is the column name
            if camp_id:  # Check if camp_id exists in the row
                camp_ids.add(camp_id)

    return camp_ids


res = extract_unique_camp_ids('./pipelines/google_daily/data/merged/ad_stats_campaign_stats_ad_history.csv')

print(res)