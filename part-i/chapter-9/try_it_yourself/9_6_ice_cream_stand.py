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

class IceCreamStand(Restaurant):
    """Represent aspect of a restaurant specific to ice cream stand"""

    def __init__(self,restaurant_name, cuisine_type):
        """Initialise attributes of the parent class
        Then initialise attribute specific to icecream stand
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['choc','vanilla', 'strawberry']

    def icecream_flavours(self):
        """Display icecream flavours"""
        print(f"Here are the ice cream flavours we serve: {self.flavours}")

icecream_place=IceCreamStand('Creamery', 'ice cream')
icecream_place.describe_restaurant()
icecream_place.open_restaurant()
icecream_place.icecream_flavours()