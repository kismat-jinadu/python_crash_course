import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename='data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #get dates and rainfall from this file.
    dates,rainfalls =[], []
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        try:
            rainfall =float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            rainfalls.append(rainfall)

#plot the rainfall
plt.style.use('seaborn')
fig,ax =plt.subplots()
ax.plot(dates,rainfalls, c='red', alpha =0.5)
ax.fill_between(dates,rainfalls, facecolor = 'blue', alpha = 0.1)

#format plot.
ax.set_title("Daily Rainfall - 2018,Sitka, CA",fontsize =20)
ax.set_xlabel('',fontsize =16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall (in)",fontsize = 16)
ax.tick_params(axis = 'both',which = 'major',labelsize=16)

plt.show()