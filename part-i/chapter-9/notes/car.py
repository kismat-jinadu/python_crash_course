class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialise attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatlyy formatted descriptive name."""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())



