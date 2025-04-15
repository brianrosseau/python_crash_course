# Exercise 9-1
class Restaurant:
    """Respresents a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes the restaurant's name and its cuisine type."""
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Lorie's Cafe", "the best food you've ever tasted")

print(f"My wife's restaurant is called {restaurant.restaurant_name}.")
print(f"The cuisine type is {restaurant.cuisine_type}.")

restaurant.describe_restaurant()
restaurant.open_restaurant()

# Exercise 9-2
# Create two more instances from the same class
restaurant_1 = Restaurant('Olive Garden', 'Italian')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('S&S', 'Southern-style cooking')
restaurant_2.describe_restaurant()

