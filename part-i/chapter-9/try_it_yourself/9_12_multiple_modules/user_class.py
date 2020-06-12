class User:
    """to creat user info"""

    def __init__(self, first_name,last_name):
        """initialise first and last name"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """describe and print user info"""
        print(f"User information: {self.first_name.title()} {self.last_name.title()}")

    def greet_user(self):
        """greet users"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}, nice to meet you.")