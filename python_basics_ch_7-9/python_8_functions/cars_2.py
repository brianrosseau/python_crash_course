# The code in this file and in cars_function.py are from cars.py 
#  The file cars_function.py is a module from which we will import functions
#  into this file.

# import module_name
import cars_function

car = cars_function.make_car('subaru', 'outback',
               color='blue',
               tow_package=True)
print(car)

# from module_name import function_name
from cars_function import make_car

car = make_car('subaru', 'outback',
               color='blue',
               tow_package=True)
print(car)

# from module_name import function_name as fn
from cars_function import make_car as mc

car = mc('subaru', 'outback',
               color='blue',
               tow_package=True)
print(car)

# import module_name as mn
import cars_function as cf

car = cf.make_car('subaru', 'outback',
               color='blue',
               tow_package=True)
print(car)

# from module_name import *
from cars_function import *

car = make_car('subaru', 'outback',
               color='blue',
               tow_package=True)
print(car) 