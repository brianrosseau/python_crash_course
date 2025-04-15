from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

def get_weather_data(path, dates, highs, lows, date_index, high_index,
                     low_index, name_index):
    """Get the highs and low from a data file."""
    lines = path.read_text(encoding='utf-8').splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')

    # Extract dates, and high and low temperatures.
    for row in reader:
        # Grab the station name, if it's not already set.
        if not place_name:
            place_name = row[name_index]
        
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Get weather data for Sitka.
path = Path('weather_data/sitka_weather_2021_simple.csv')
dates, highs, lows = [], [], []
place_name = ""
get_weather_data(path, dates, highs, lows, date_index, high_index,
                     low_index, name_index)

# Plot the high and low temperatures for Sitka.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.6)
ax.plot(dates, lows, color='blue', alpha=0.6)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# Get weather data for Death Valley.
path = Path('weather_data/death_valley_2021_full.csv')
dates, highs, lows = [], [], []
place_name = ""
get_weather_data(path, dates, highs, lows, date_index, high_index,
                     low_index, name_index)

# Add the high and low temperatures for Death Valley to the current plot.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.3)
ax.plot(dates, lows, color='blue', alpha=0.3)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

# Format plot.
title = "Daily high and low temperatures - 2021"
title += "\nSitka, AK and Death Valley, CA"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
ax.set_ylim(10, 135)

plt.show()