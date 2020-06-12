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

class Privileges:
    """to store admin privileges"""

    def __init__(self, privileges=['you can add post','you can delete post', 'you can ban user']):
        """initialise privileges"""
        self.privileges = privileges
        
        
    def show_privileges(self):
        """print admin privileges"""
        print(f"You have admin privileges. These are:")
        for privilege in self.privileges:
            print(f"\t{privilege}")

class Admin(User):
    """Represent aspects of user specific to admin"""

    def __init__(self, first_name,last_name):
        """initialise attributes of the parent class.
        Then initialise attributes specific to admin.
        """
        super().__init__(first_name,last_name)
        self.privileges = Privileges()