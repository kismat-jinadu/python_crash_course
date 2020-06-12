class Restaurant:
    """describe different types of restaurant"""

    def __init__(self,restaurant_name, cuisine_type):
        """Initialise restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number = 0

    def describe_restaurant(self):
        """display restaurant description"""
        print(f"This restaurant is called {self.restaurant_name}")
        print(f"It is a {self.cuisine_type} restaurant")

    def open_restaurant(self):
        """display if the restaurant is open"""
        print(f"{self.restaurant_name} is open for business")

    def number_served(self):
        """display number served"""
        print(f"The number of customers served = {self.number}")
        

restaurant = Restaurant('Chop-Chop','burger')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served()

### set number served


class Restaurant:
    """describe different types of restaurant"""

    def __init__(self,restaurant_name, cuisine_type):
        """Initialise restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number = 0

    def describe_restaurant(self):
        """display restaurant description"""
        print(f"This restaurant is called {self.restaurant_name}")
        print(f"It is a {self.cuisine_type} restaurant")

    def open_restaurant(self):
        """display if the restaurant is open"""
        print(f"{self.restaurant_name} is open for business")

    def number_served(self):
        """display number served"""
        print(f"The number of customers served = {self.number}")

    def set_number_served(self, number):
        """set the number that have been served"""
        self.number = number
        

restaurant = Restaurant('Chop-Chop','burger')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(5)
restaurant.number_served()

## add increment

class Restaurant:
    """describe different types of restaurant"""

    def __init__(self,restaurant_name, cuisine_type):
        """Initialise restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number = 0

    def describe_restaurant(self):
        """display restaurant description"""
        print(f"This restaurant is called {self.restaurant_name}")
        print(f"It is a {self.cuisine_type} restaurant")

    def open_restaurant(self):
        """display if the restaurant is open"""
        print(f"{self.restaurant_name} is open for business")

    def number_served(self):
        """display number served"""
        print(f"The number of customers served = {self.number}")

    def set_number_served(self, number):
        """set the number that have been served"""
        self.number = number

    def increment_number_served(self, number):
        """add number of customers served per day"""
        self.number += number
        

restaurant = Restaurant('Chop-Chop','burger')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(5)
restaurant.number_served()
restaurant.increment_number_served(100)
print(f"\nCheck end of day figure:")
restaurant.number_served()