#Importing Classes

# Importing Multiple Classes from a Module
from cars import Car, ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# Importing an Entire Module
import cars

my_mustang = cars.Car('ford', 'mustang', 2024)      # Add module name with dot notation
print(my_mustang.get_descriptive_name())
my_leaf = cars.ElectricCar('nissan', 'leaf', 2024)  # Add module name with dot notation
print(my_leaf.get_descriptive_name())

