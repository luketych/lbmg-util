import csv

def calculate_total_for_camp_id(csv_file, camp_id, columns):
    totals = {column: 0 for column in columns}
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row.get('camp_id') == camp_id:
                for column in columns:
                    value = float(row.get(column)) if row.get(column) else 0
                    totals[column] += value

    print(f"Total for Camp ID: {camp_id}")
    for column, total in totals.items():
        print(f"{column}: {total}")


calculate_total_for_camp_id('./pipelines/google_daily/data/merged/ad_stats_campaign_stats_ad_history.csv', '227940.0', ['clicks_x', 'clicks_y', 'conversions_x', 'conversions_y', 'impressions_x', 'impressions_y', 'interactions_x', 'interactions_y'])