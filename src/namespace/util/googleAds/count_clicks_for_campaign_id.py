import csv


def calculate_total_stats(input_file):
    total_stats = {}
    
    with open(input_file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            ad_group_id = row['ad_group_id']
            campaign_id = row['campaign_id']
            clicks = float(row['clicks'])
            conversions = float(row['conversions'])
            impressions = float(row['impressions'])
            interactions = float(row['interactions'])
            
            if campaign_id in total_stats:
                total_stats[campaign_id]['clicks'] += clicks
                total_stats[campaign_id]['conversions'] += conversions
                total_stats[campaign_id]['impressions'] += impressions
                total_stats[campaign_id]['interactions'] += interactions
            else:
                total_stats[campaign_id] = {
                    'ad_group_id': ad_group_id,  
                    'campaign_id': campaign_id, 
                    'clicks': clicks,
                    'conversions': conversions,
                    'impressions': impressions,
                    'interactions': interactions
                }
    
    sorted_total_stats = dict(sorted(total_stats.items(), key=lambda x: x[1]['clicks'], reverse=True))
  
    return sorted_total_stats
  
  
res = calculate_total_stats('./pipelines/google_daily/data/download/ad_stats.csv')