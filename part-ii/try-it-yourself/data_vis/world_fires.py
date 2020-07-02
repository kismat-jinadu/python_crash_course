import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

num_rows = 20_000

filename='data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, brightnesses, lats, lons = [], [],[], []
    hover_texts = []
    row_num = 0
    for row in reader:
        date = datetime.strptime(row[5],'%Y-%m-%d')
        brightness = float(row[2])
        lat = row[0]
        lon =row[1]
        hover_text = f"{date.strftime('%m/%d/%y')} - {brightness}"

        dates.append(date)
        brightnesses.append(brightness)
        lats.append(lat)
        lons.append(lon)
        hover_texts.append(hover_text)

        row_num += 1
        if row_num == num_rows:
            break

#Map the fires.
data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[brightness/30 for brightness in brightnesses],
        'color':brightnesses,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'},
    },
}]
my_layout = Layout(title="World Fires 7 day")

fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='world_fires.html')