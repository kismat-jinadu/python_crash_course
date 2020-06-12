alien_0={'colour':'green', 'points':5}

print(alien_0['colour'])
print(alien_0['points'])

#adding new key-value pairs

alien_0 ={'colour':'green','points':5}
print(alien_0)

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#starting with emoty dictionary

alien_0={}
alien_0['colour']='green'
alien_0['points']=5
print(alien_0)

#modifying values in a dictionary

alien_0={'colour':'green'}
print(f"The alien is {alien_0['colour']}.")

alien_0['colour']='yellow'
print(f"The alien is now {alien_0['colour']}.")

###
alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original position:{alien_0['x_position']}")
#move the alien to the right.
#determine how far to move the alien based on its current speed.
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    #This must be a fast alien.
    x_increment=3
#the new position is the old position plus the increment. 
alien_0['x_position']=alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

#removing key-value pairs

alien_0={'colour':'green','points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

