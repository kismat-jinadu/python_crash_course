import plotly.express as px

from random_walk import RandomWalk 


#make a random walk
rw= RandomWalk(50_000)
rw.fill_walk()

fig = px.scatter(x=rw.x_values, y=rw.y_values)
fig.show()