# Exercise 9-12b to be used with user_only_module.py and multiple_modules.py

# A Module containing Privileges and Admin classes

# must begin my importing parent class from the parent class module
from user_only_module import User

class Admin(User):
    """Represts aspects of a user, specific to an administrator."""

    def __init__(self, first_name, last_name, username, email):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to a administrator.
        """
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges()

# Related class
class Privileges:
    """A class to model unique user privileges of an administrator."""
    
    def __init__(self, privileges=[]):
        """Initialize the attributes."""
        self.privileges = privileges
    
    def show_privileges(self):
        """Lists the administrator's set of privileges."""
        print("\nThe administrator has the following privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"\t-{privilege.capitalize()}")
        else:
            print("\tNo unique privileges.")
