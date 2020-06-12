pizzas=['chicken pizza','beef pizza','tuna pizza']
for pizza in pizzas:
    print(f"I like {pizza}")
print("I really love pizza")

friend_pizzas=pizzas[:]
print("My favourite pizzas are:")
for pizza in pizzas: 
  print(pizza.title())
print("\nMy friend's favourite pizzas are:")
for friend_pizza in friend_pizzas: 
  print(friend_pizza.title())

pizzas.append('cheese pizza')
friend_pizzas.append('veggie pizza')
print("\nMy favourite pizzas are:")
for pizza in pizzas: 
  print(pizza.title())
print("\nMy friend's favourite pizzas are:")
for friend_pizza in friend_pizzas: 
  print(friend_pizza.title())