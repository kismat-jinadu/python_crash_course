from user_class import User

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