odd_numbers = list(range(1, 21, 2))
for odd in odd_numbers:
    print(odd)

threes = list(range(3, 31, 3))
for third in threes:
    print(third)

cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)
print(cubes)

#use list comprehension to do the same thing
cubes = [number**3 for number in range(1,11)]
print(cubes)