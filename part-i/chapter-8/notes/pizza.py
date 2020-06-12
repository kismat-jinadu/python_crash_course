def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

#the asterisks it to tell python ro make empty tuple called toppings. a call can be made of
#different number of arguments

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers', 'extra cheese')

#

def make_pizza(*toppings):
    """Summarise the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers', 'extra cheese')

#

def make_pizza(size,*toppings):
#place parameter with arbituary number of arguments last
    """Summarise the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers', 'extra cheese')