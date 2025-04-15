# RETURN VALUES (continued)
#  Returning a Dictionary

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# we can extend the function to include any other information as well
# here we add age...
def build_person(first_name, last_name, age=None):   #None is a special value used when a variable has no specific value assigned to it. It is like a placeholder value. None evaluates to False in conditional tests.
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age     #now, if the function call includes a value for age, the value is stored in the dictionary
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# the function can be modified to store any other information you want about 
#  the person, like middle name or occupation.

