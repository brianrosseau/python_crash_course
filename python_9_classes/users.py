class User:
    """Represents a company user."""
    def __init__(self, first_name, last_name, username, email):
        """Initialize first and last name attributes for user."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

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
              
user_0 = User('brian', 'rosseau', 'brosseau', 'brosseau@yoyo.com')

user_0.describe_user()
user_0.greet_user()

user_1 = User('lorie', 'rosseau', 'lrosseau', 'lrosseau@yoyo.com')

user_1.describe_user()
user_1.greet_user()

user_2 = User('able', 'rosseau', 'ablerosseau', 'ablerosseau@yoyo.com')

user_2.describe_user()
user_2.greet_user()