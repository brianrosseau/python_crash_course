from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/san_francisco_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

print(header_row)

# Automatically determine the indexes for date and high and low values.
for index, column_name in enumerate(header_row):
    print(index, column_name)
    if column_name == 'DATE':
        d = index
    if column_name == 'TMAX':
        h = index
    if column_name == 'TMIN':
        l = index
    if column_name == 'NAME':
        n = index

print(h,l)

# Extract dates, and high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[d], '%Y-%m-%d')
    high = int(row[h])
    low = int(row[l])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# print(dates)
print(highs)
print(lows)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
year = datetime.strptime(d, '%Y')
name = n 
title = f"Daily High and Low Temperatures" {year} \n {n}
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

# Set y-axis range for comparison with other plots.
plt.ylim(10, 135)

plt.show()
