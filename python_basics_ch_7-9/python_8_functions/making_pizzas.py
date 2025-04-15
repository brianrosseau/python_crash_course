# 1. Importing an entire module
#  import module_name
import pizza_function

#  module_name.function_name()
pizza_function.make_pizza(16, 'pepperoni')
pizza_function.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 2. Importing specific functions from a module
#  from module_name import function_name
#    or import multiple functions...
#  from module_name import function_name_0, function_name_1, function_name_2
from pizza_function import make_pizza

# no need for the dot notation
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 3. Using 'as' to Give a FUNCTION an Alias
#  from module_name import function_name as fn
from pizza_function import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 4. Using 'as' to give a MODULE an Alias
#  import module_name as mn

import pizza_function as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 5. Import all functions in a module using *
#  from module_name import *
from pizza_function import *

# no need for the dot notation
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# However, best not to use this approach if importing large modules you didn't write,
#   as some of the imported functions may be confused with my written functions.

# Best practice is to import the function(s) you want, or import the entire 
#   module and use dot notation.

