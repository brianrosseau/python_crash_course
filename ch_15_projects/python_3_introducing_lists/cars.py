# Sort a list PERMANENTLY with the sort() METHOD
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# the sort() method sorts the list alphabetically. THIS IS A PERMANENT CHANGE.

# you can sort in reverse order as well.
cars.sort(reverse = True)
print(cars)

# Sort a list TEMPORARILY with the sort() FUNCTION
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print(sorted(cars, reverse=True))

# Use the reverse() method to print an original list in reverse order (that is, last to first)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# do reverse() method again to revert back to original list
cars.reverse()
print(cars)

# Use the len() function to find the length of a list
len(cars)