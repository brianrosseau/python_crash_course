# import randint function from the random module
# Random module is part of the Python Standard Library

# tip: do not name my file the same name as a module in the Python Standard Library.
#   for instance, if I named my file 'random', I would get an ImportError
#   because there is already a file (module) in the Python Standard Library 
#   with that name. Thus, I called my file 'my_random.py', not 'random.py'

from random import randint
# this function generates a random number between (and including) 1 and 6.
randint(1, 6)


# The choice function takes a list or a tuple and returns a randomly chosen element.
from random import choice
players = ['charles', 'marting', 'michael', 'florence', 'eli']
first_up = choice(players)
first_up

