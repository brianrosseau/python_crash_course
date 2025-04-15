# Tuples are simple data structures. Use tuples when you want to store a set of values that should not be changed throughout the life of the program.


#Working with TUPLES. Similar to lists, but tuples use parentheses (although not necessary) instead of square brackets.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Tuples are immutable !!!!!!!!!!! They cannot be changed, unlike lists, which are frequently changed.
dimensions[0] = 250
# if you try to change a tuple, you get an error

# the parentheses make tuples more readable, but are not necessary. Tuples are technically defined by the presence of a comma.

# you can even make a tuple with one element, using a trailing comma...
my_t = (3,)
print(my_t)

#using a for loop (same as then looping through a list)
for dimension in dimensions:
    print(dimension)

#while you cannot modify a tuple, you can redefine the variable that represents the tuple.
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nNew dimensions:")
for dimension in dimensions:
    print(dimension)

