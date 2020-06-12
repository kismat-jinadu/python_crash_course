my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

print("\nMy favourite foods are:")
for my_food in my_foods:
    print(my_food.title())

print("\nMy friend's favourite foods are:")
for friend_food in friend_foods:
    print(friend_food.title())