#add update method
#add logic 

class Car:

    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 13

    def get_descriptive_name(self):
        """Return a neatlyy formatted descriptive name."""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(20)
my_new_car.read_odometer()