# RETURN VALUES
#   MAKING AN ARGUMENT OPTIONAL
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


#    MAKING AN ARGUMENT OPTIONAL
def get_formatted_name(first_name, middle_name, last_name):     #what if we want to add a middle name
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
# this function works well when we give a first, middle, and last name

# however, middle names are not always needed
# if you tried to call the above code w/o a middle name it would give an error
musician = get_formatted_name('john', 'hooker')

# to make middle name optional, we give it an empty default value in the definition
def get_formatted_name(first_name, last_name, middle_name=''):     #default values must be listed last
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')          #note middle name is given last bc this is how the function is written
print(musician)
