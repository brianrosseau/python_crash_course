# Exercise 9-11a to be used with imported_admin.py

# Module for User, Privileges, and Admin classes


class User:
    """Represents a company user."""
    
    def __init__(self, first_name, last_name, username, email):
        """Initialize first and last name attributes for user."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        # Add attribute and set default to zero
        self.login_attempts = 0

    def describe_user(self):
        """Summarizes user information"""
        print(f'''
              \nUser Summary:
              \tFirst name: \t{self.first_name.title()}
              \tLast name: \t{self.last_name.title()}
              \tUsername: \t{self.username}
              \tEmail: \t\t{self.email}
            ''')
    
    def greet_user(self):
        """Prints a personalized greeting to the user"""
        print(f"Hello, {self.first_name.title()}!")

    def read_login_attempts(self):
        """Reads total number of login attempts."""
        print(f"Login attempts: {self.login_attempts}")

    def increment_login_attempts(self):
        """Increments total number of login attempts by one."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets number of login attempts to zero."""
        self.login_attempts = 0

# Child class
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