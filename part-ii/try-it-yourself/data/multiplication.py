
from plotly.graph_objs import Bar,Layout
from plotly import offline

from die import Die

#create two D6s
die_1 = Die()
die_2 = Die()

#make some rolls, and store results in a list.
results = []
for roll_num in range(10000):
    #using multiplication instead of addition
    result = die_1.roll() * die_2.roll()
    results.append(result)

#analyze the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1,max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visualise the results.
x_values = list(range(1,max_result +1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Result','dtick':1}
y_axis_config = {'title':'Frequency of Result'}
my_layout = Layout(title = 'Results of rolling two D6s and multiplying the result',
xaxis=x_axis_config, yaxis = y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6xd6.html')
