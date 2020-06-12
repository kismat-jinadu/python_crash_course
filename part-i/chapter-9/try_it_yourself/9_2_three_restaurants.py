class Restaurant:
    """describe different types of restaurant"""

    def __init__(self,restaurant_name, cuisine_type):
        """Initialise restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """display restaurant description"""
        print(f"This restaurant is called {self.restaurant_name}")
        print(f"It is a {self.cuisine_type} restaurant")

    def open_restaurant(self):
        """display if the restaurant is open"""
        print(f"{self.restaurant_name} is open for business")

restaurant = Restaurant('KFC','chicken')
restaurant.describe_restaurant()

restaurant = Restaurant('Dominos','pizza')
restaurant.describe_restaurant()

restaurant = Restaurant('Mr Chow','chicken')
restaurant.describe_restaurant()