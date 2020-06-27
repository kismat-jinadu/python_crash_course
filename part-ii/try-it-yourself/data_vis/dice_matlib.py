
import matplotlib.pyplot as plt
import numpy as np

from die import Die

#create a D6 and a D10
die_1 = Die()
die_2 = Die(10)

#make some rolls, and store results in a list.
results = []
for roll_num in range(50_000):
    result = die_1.roll() +die_2.roll()
    results.append(result)


max_result = die_1.num_sides + die_2.num_sides

plt.hist(results, bins=np.arange(2,max_result +1))

#set chart title and label axes.
plt.title("Results of rolling a D6 and D10 50000 times", fontsize =10)
plt.xlabel("Result",fontsize =14)
plt.ylabel("Frequency of Result", fontsize =14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

#visualise the results.

plt.show()
