# Creating a Dog Class
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):  # create a method (a function that is part of a class is called a method.)
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):    # create a method
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Making an Instance from a Class
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age} years old.")

my_dog = Dog('Able', 8)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Flower', 11)
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()

