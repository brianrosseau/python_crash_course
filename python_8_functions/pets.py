# POSITIONAL ARGUMENTS
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'able')         # call the function as often as you like

# order matters in positional arguments: if you reverse them you will get funny results
describe_pet('harry', 'hamster')

# KEYWORD ARGUMENTS
describe_pet(animal_type='hamster', pet_name='harry')
# here we explicitly tell the function which argument belongs to which parameter.
# we can write it backwards and get the same result. This way, order doesn't matter.
describe_pet(pet_name='harry', animal_type='hamster')

# DEFAULT VALUES
def describe_pet(pet_name, animal_type='dog'): # set a default value in the function definition
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')     # no need to put in the animal_type if it matches the default

#if you find that 'dog' is commonly passed as an argument to this function,
#  you can set it as the default value in the function definition.
#  This simplifies the function call

# NOTE: in the function definition, the parameter(s) that are not set to a 
#        default value go first ('pet_name'). This is because Python still
#        interprets the argument as a positional argument.

describe_pet('willie')

# to describe an animal_type other than the default, use the keyword argument...
describe_pet(pet_name='harry', animal_type='hamster')
# ... or just add a second positional argument that overrides the default
describe_pet('harry', 'hamster')

# EQUIVALENT FUNCTION CALLS 
# so then all of the following calls would work for this function:

# A dog named Willie...
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry...
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


# if we try to call a function that has parameters, without providing arguments
#   (unless all the parameters have default values), we get an error
describe_pet()