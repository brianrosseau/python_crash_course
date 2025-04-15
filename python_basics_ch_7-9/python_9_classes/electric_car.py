# INHERITANCE
# The __init__() Method for a Child Class

#  We begin with the parent class. When you create a child class, the parent
#   class must be part of the current file and must appear before the child
#   class in the file.

# Parent Class
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statment showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

# Child Class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Intitialize attributes of the parent class."""
        super().__init__(make, model, year)
        # the super() function allows you to call a method from a parent class.
        # here, it calls the __init__() method from Car, giving ElectricCar 
        #   all the attributes of the parent class Car.

# this test shows that the attributes of the parent class are in the child class.
my_leaf = ElectricCar('nissan', 'leaf', '2024')
print(my_leaf.get_descriptive_name())

# Defining Attributes and Methods for the Child Class

class ElectricCar(Car):
    """Represents aspects of a car, specific to an electric vehicle."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        # Add a new attribute
        self.battery_size = 40

    # Add a method to report on the new attribute
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# test the new method
my_leaf.describe_battery()


# Overriding Methods from the Parent Class

# to override a method in a parent class, write a method in the child class with
#  the same name as the method in the parent class you want to override.
#  So, if the parent class has a method called fill_gas_tank(), you would write
#  an overriding method in the child class with same name that.

'''
class ElectricCar(Car):
 --snip--

    def fill_gas_tank(self):
    """Electric cars don't have gas tanks."""
    print("This car doesn't have a gas tank!")
'''


# Instances as Attributes

# if you find your class getting lengthy as you add more and more attributes
#   and methods to it, you can stop and move those attributes and methods that 
#   are alike to a separate class.

# For example, instead of adding lots of attributes and methods about the battery
#   to the ElectricCar class, you can make a separate class called 'Battery'
#   that houses that information. 
#   Then you can use a Battery instance as an attribute in the ElecticCar class.

'''
class Car:
    --snip--
'''

# Move battery info from the ElectricCar child class into a newly created class called Battery.
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):    # battery_size parameter is optional
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    # The method describe_battery() is moved from ElectricCar to this class.
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    # We'll add another method about batteries, too.
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represents aspects of a car, specific to an electric vehicle."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        # Add a Battery instance as an attribute in ElecticCar class
        # All ElectricCar instances will now have a Battery instance created automatically!!
        self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

my_leaf.battery.describe_battery()  # Call the method through the battery attribute
my_leaf.battery.get_range()         # Call the method through the battery attribute