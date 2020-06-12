class User:
    """to creat user info"""

    def __init__(self, first_name,last_name):
        """initialise first and last name"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """describe and print user info"""
        print(f"User information: {self.first_name.title()} {self.last_name.title()}")

    def greet_user(self):
        """greet users"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}, nice to meet you.")

    def number_login_attempts(self):
        """Display login attempts"""
        print(f"The number of login attempts = {self.login_attempts}")


    def increment_login_attempts(self, login_attempts):
        """add new login attempts"""
        self.login_attempts += login_attempts

    def reset_login_attempts(self,login_attempts):
        """reset login attempts"""
        self.login_attempts = login_attempts

user= User('tola','jimoh')
user.describe_user()
user.greet_user()
user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.number_login_attempts()

user.reset_login_attempts(0)
user.number_login_attempts()