from car_4 import Car

my_new_car=Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


### you can do multiple importation

from car_4 import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

### import entire module then access class using dot

import car_4

my_french_car = car_4.Car('renault','megane',2010)
print(my_french_car.get_descriptive_name())

my_tesla = car_4.ElectricCar('tesla','roadster',2020)
print(my_tesla.get_descriptive_name())

## to import all classes from a module "from module_name import*"
## but it is not recommended to do this