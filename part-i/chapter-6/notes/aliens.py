#nesting
alien_0={'colour':'green', 'points':5}
alien_1={'colour':'yellow', 'points':10}
alien_2={'colour':'red', 'points':15}

aliens=[alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#for a large number of aliens we use range()
#make an empty list for storing aliens

aliens=[]

#make 30 green aliens.
for alien_number in range(30):
    new_alien={'colour':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

#show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created.
print(f"Total number of aliens:{len(aliens)}")

#make an empty list for storing aliens

aliens=[]

#make 30 green aliens.
for alien_number in range(30):
    new_alien={'colour':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['colour']=='green':
        alien['colour']='yellow'
        alien['speed']='medium'
        alien['points']=10

#show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")