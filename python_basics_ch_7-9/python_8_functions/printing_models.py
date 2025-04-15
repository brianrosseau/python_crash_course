# Passing a List to a function (continued)
#  Modifying a List in a Function

# 1. the following code does not use a function...

# Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)


# 2. We can reorganize the above code by writing two functions...
def print_models(unprinted_designs, completed_models):      # Function One
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:                                # with same code as above
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):                # Function Two
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")      # with same code as above
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)           # Call Function One
show_completed_models(completed_models)                     # Call Function Two

# This program with the two functions has the same output as the program 
#  without the functions, but it is more organized and is easier to extend 
#  and maintain than the code without the functions.
#  If we need to print more designs later on, we can simply call print_models() again.
