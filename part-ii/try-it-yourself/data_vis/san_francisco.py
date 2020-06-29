import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename='data/san_fran_2018.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #get dates, high and low temperatures from this file.
    dates,highs, lows =[], [], []
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        try:
            high =int(row[3])
            low =int(row[4])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#plot the high and low temperatures.
plt.style.use('seaborn')
fig,ax =plt.subplots()
ax.plot(dates,highs, c='red', alpha =0.5)
ax.plot(dates,lows, c='blue', alpha =0.5)
ax.fill_between(dates,highs,lows, facecolor = 'blue', alpha = 0.1)

#format plot.
title="Daily high and low temperatures - 2018\nSan Francisco,CA"
ax.set_title(title,fontsize=20)
ax.set_xlabel('',fontsize =16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)",fontsize = 16)
ax.tick_params(axis = 'both',which = 'major',labelsize=16)

#change y axis range so it can be compared with death valley plot
plt.ylim(20,130)

plt.show()