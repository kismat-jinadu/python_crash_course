import matplotlib.pyplot as plt 

from random_walk import RandomWalk 

#keep making new walks, as long as the program is active.

while True:
    #make a random walk
    rw= RandomWalk()
    rw.fill_walk()

    #plot the points in the walk.
    plt.style.use('classic')
    fig,ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth = 3)

  
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break