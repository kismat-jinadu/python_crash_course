from car_5 import Car

from electric_car_5 import ElectricCar

my_beetle = Car('volkswagen','beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())


## Aliases can be used eg

from electric_car_5 import ElectricCar as EC 

my_tesla = EC('tesla','roadster_2',2020)
print(my_tesla.get_descriptive_name())