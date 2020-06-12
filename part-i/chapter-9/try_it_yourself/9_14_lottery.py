
numbers=range(1,11)
pick= ['a','d','f','g','m']

#merge the numbers and letters
for number in numbers:
    if number not in pick:
        pick.append(number)

from random import choice 

select_1 = choice(pick)
select_2 = choice(pick)
select_3 = choice(pick)
select_4 = choice(pick)

print("The winning lottery ticket is:")
print(f"\t{select_1}, {select_2}, {select_3}, {select_4}")