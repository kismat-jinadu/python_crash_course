import pizza_2

pizza_2.make_pizza(16,'pepperoni')
pizza_2.make_pizza(12,'mushrooms','green peppers','extra cheese')

#to import just a function from another module:

from pizza_2 import make_pizza

make_pizza(14,'chicken')
make_pizza(16,'beef','onions','olives')

#you can use alias in case you already have function with same name

from pizza_2 import make_pizza as mp

mp(14,'tuna')
mp(16,'chicken','onions','olives')

#can also use alias for the module

import pizza_2 as p

p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')

#to import all functions from a module.use asterisks
#doing this, you dont need dot to call function
#but it is not advised to use this method. dot method is better

from pizza_2 import *

make_pizza(16,'pepperoni','beef')
make_pizza(12,'mushrooms','green peppers','extra cheese')