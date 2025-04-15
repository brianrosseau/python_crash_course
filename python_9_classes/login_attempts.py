# Exercise 9-5

# Start with program from users.py and add an attribute called login_attemps
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

    # Add method that reads number of login attempts.
    def read_login_attempts(self):
        """Reads total number of login attempts."""
        print(f"Login attempts: {self.login_attempts}")

    # Add method that increments number of login attempts.
    def increment_login_attempts(self):
        """Increments total number of login attempts by one."""
        self.login_attempts += 1

    # Add method that resets number of login attempts to zero.
    def reset_login_attempts(self):
        """Resets number of login attempts to zero."""
        self.login_attempts = 0
              
user_0 = User('brian', 'rosseau', 'brosseau', 'brosseau@yoyo.com')

user_0.describe_user()
user_0.greet_user()

user_0.read_login_attempts()

user_0.increment_login_attempts()
user_0.read_login_attempts()
user_0.increment_login_attempts()
user_0.read_login_attempts()

user_0.reset_login_attempts()
user_0.read_login_attempts()