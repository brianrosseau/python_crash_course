# the remove() function removes the first of a specific value from a list.

# Using a while loop with the remove() function allows you to remove all of that specific value.

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

'''
sorted(pets)        # This sorts the list alphabetially
set(pets)           # This prints a set of unique values from the list
'''

while 'cat' in pets:
    pets.remove('cat')

print(pets)