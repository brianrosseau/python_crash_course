from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract dates and rainfall amounts (PRCP).
dates, prcp = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    current_rainfall = float(row[3])
    dates.append(current_date)
    prcp.append(current_rainfall)

# Plot the rainfall.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcp, color='green')

# Format plot.
ax.set_title("Daily Rainfall Amounts, 2021\nDeath Valley, CA", fontsize=20)
ax.set_xlabel('', fontsize=13)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation (mm)", fontsize=13)
ax.tick_params(labelsize=13)

plt.show()