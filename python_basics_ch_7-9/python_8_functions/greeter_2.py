# RETURN VALUES (continued)
#   USING A FUNCTION WITH A WHILE LOOP
#  this builds off of the function in the 'formatted_name.py' file 

# 1. here is a first attempt at adding a while loop to a function...
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# because there is no break, the above code will forever ask for a name

# 2. Second attempt: must add breaks to offer ways to exit the loop at any prompt.
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")    # prompt notifying of quit option

    f_name = input("First name: ")
    if f_name == 'q':                           # add break
        break

    l_name = input("Last name: ")
    if l_name == 'q':                           # add break
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
    