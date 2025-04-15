# The code in this file and in printing_functions.py are from printing_models.py 
#  The file printing_functions.py is a module from which we will import functions
#  into this file.
import printing_functions as pf

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)           # Call Function One
pf.show_completed_models(completed_models)                     # Call Function Two

# This program with the two functions has the same output as the program 
#  without the functions, but it is more organized and is easier to extend 
#  and maintain than the code without the functions.
#  If we need to print more designs later on, we can simply call print_models() again.

