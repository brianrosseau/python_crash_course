# Exercise 9-4

# Start with program in Ex9-1 restaurant.py and add attribute with default value.
class Restaurant:
    """Respresents a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0               # Add attribute with default value

    def describe_restaurant(self):
        """Describes the restaurant's name and its cuisine type."""
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def read_number_served(self):           # 0. Create method that reads number of customers served.
        """Prints a message telling the total number of customers served."""
        print(f"{self.restaurant_name} has served {self.number_served} customers.")

    def set_number_served(self, set_number_served): # 2. Add method that sets new value for customers served.
        """
        Lets you set the total number of customers served to a given value.
        Reject the change if it decreases the number of customers served.
        """
        if set_number_served >= self.number_served:
            self.number_served = set_number_served
        else:
            print("The total number served cannot be decreased.")

    def increment_number_served(self, add_number_served):   # 3. Add method that adds to customer total incrementally.
        """Add the given amount to the total number of customers served."""
        self.number_served += add_number_served

restaurant = Restaurant("Lorie's Cafe", "the best food you've ever tasted")

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.read_number_served()             # 0. Read current value

restaurant.number_served = 50               # 1. Modify value directly
restaurant.read_number_served()             # 0. Read current value

restaurant.set_number_served(121)           # 2. Modify value through method with set value
restaurant.read_number_served()
restaurant.set_number_served(113)           # If statement rejects decreasing total.
restaurant.read_number_served()

restaurant.increment_number_served(14)      # 3. Add to total incrementally through method.
restaurant.read_number_served()
restaurant.increment_number_served(1_234)
restaurant.read_number_served()