#!/usr/bin/python3

import json
from datetime import datetime
import pandas as pd

# Print start time
current_time = datetime.now()
print(f"\nStarted SMA Script on: {current_time.strftime('%x %X')}\n")

# Load gecko analysis data
json_in_addr = 'data/geckoAnalysis.json'

with open(json_in_addr, 'r') as f:
    gecko_data = json.load(f)

gecko_keys = list(gecko_data.keys())

# Define the moving average periods
moving_avg_periods = [3, 7, 14, 30, 50, 90, 200]

for gecko_key in gecko_keys:
    current_data = gecko_data[gecko_key]
    token_data = current_data['data']

    # Convert token_data to a pandas Series
    prices = pd.Series(token_data)
    prices.index = pd.to_datetime(prices.index)
    prices.sort_index(inplace=True)  # Ensure the index is sorted

    # Calculate moving averages
    for period in moving_avg_periods:
        ma_series = prices.rolling(window=period, min_periods=1).mean()

        # Convert the moving average series back to the desired dictionary format
        ma_dict = ma_series.round(2).dropna().to_dict()
        ma_dict_str_keys = {date.strftime('%Y-%m-%d'): value for date, value in ma_dict.items()}

        # Add the moving average data to the current data dictionary
        current_data[f'movingAvg{period}'] = ma_dict_str_keys

        print(f"Added {period}-day SMA for: {current_data.get('pair', gecko_key)}")

# Print completion time
current_time = datetime.now()
print(f"\nCompleted on: {current_time.strftime('%x %X')}\n")

# Save the modified data back to JSON
json_out_addr = 'data/geckoAnalysis2.json'

try:
    with open(json_out_addr, 'w') as fp:
        json.dump(gecko_data, fp)
    print(f"\nSuccess Creating Sorted Trade JSON file at: {json_out_addr}\n")
except Exception as e:
    print(e)
