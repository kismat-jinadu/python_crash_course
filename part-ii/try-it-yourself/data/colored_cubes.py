import matplotlib.pyplot as plt 

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig,ax =plt.subplots()
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds, s=10)

#set chart title and label axes.
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize =14)
ax.set_ylabel("Square of Value", fontsize =14)

#set size of tick labels.
ax.tick_params(axis ='both', which ='major', labelsize =14)

#set the range for each axis.
ax.axis([0,5100,0,130_000_000_000])

plt.show()