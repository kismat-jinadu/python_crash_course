import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename='data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #get dates, high and low temperatures from this file.
    dates,highs, lows =[], [], []
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        try:
            high =int(row[5])
            low =int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

filename='data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #get dates, high and low temperatures from this file.
    dates_1,highs_1, lows_1 =[], [], []
    for row in reader:
        current_date_1 = datetime.strptime(row[2],'%Y-%m-%d')
        try:
            high_1 =int(row[4])
            low_1 =int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates_1.append(current_date_1)
            highs_1.append(high_1)
            lows_1.append(low_1)

#plot the high and low temperatures for sitka.
plt.style.use('seaborn')
fig,ax =plt.subplots()
ax.plot(dates,highs, c='red', alpha =0.5)
ax.plot(dates,lows, c='blue', alpha =0.5)
ax.fill_between(dates,highs,lows, facecolor = 'blue', alpha = 0.1)

#plot the high and low temperatures for death valley.
ax.plot(dates_1,highs_1, c='red', alpha =0.5)
ax.plot(dates_1,lows_1, c='green', alpha =0.5)
ax.fill_between(dates_1,highs_1,lows_1, facecolor = 'blue', alpha = 0.1)

#format plot.
title="Daily high and low temperatures - 2018\nSitka and Death Valley,CA"
ax.set_title(title,fontsize=20)
ax.set_xlabel('',fontsize =16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)",fontsize = 16)
ax.tick_params(axis = 'both',which = 'major',labelsize=16)

#change y axis range so it can be compared with death valley plot
plt.ylim(20,130)

plt.show()