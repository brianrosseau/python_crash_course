# Exercise 9-6
# Start with the Restaurant class from Exercise 9-4 number_served.py
# Add an attribute called flavors and method that describes these flavors.

class Restaurant:
    """Respresents a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0           

    def describe_restaurant(self):
        """Describes the restaurant's name and its cuisine type."""
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def read_number_served(self):
        """Prints a message telling the total number of customers served."""
        print(f"{self.restaurant_name} has served {self.number_served} customers.")

    def set_number_served(self, set_number_served):
        """
        Lets you set the total number of customers served to a given value.
        Reject the change if it decreases the number of customers served.
        """
        if set_number_served >= self.number_served:
            self.number_served = set_number_served
        else:
            print("The total number served cannot be decreased.")

    def increment_number_served(self, add_number_served):
        """Add the given amount to the total number of customers served."""
        self.number_served += add_number_served

class IceCreamStand(Restaurant):
    """Represents aspects of a restaurant, specific to ice cream stands."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize aspects of the parent class Restaurant
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        """Print a list of flavors offered."""
        print("\nAble's Gelateria offers the following ice cream flavors:")
        for flavor in self.flavors:
            print(f"\t{flavor.title()}")


'''
restaurant = Restaurant("Lorie's Cafe", "the best food you've ever tasted")
'''

able_ice_cream_stand = IceCreamStand("Able's Gelateria", 'Italian ice cream')
able_ice_cream_stand.flavors = ['vanilla', 'chocolate', 'strawberry', 'peach', 'butter pecan',]

print(able_ice_cream_stand.describe_restaurant())
print(able_ice_cream_stand.read_number_served())

able_ice_cream_stand.display_flavors()