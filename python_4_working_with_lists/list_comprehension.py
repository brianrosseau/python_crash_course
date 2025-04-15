squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

#List comprehension allows you to generate this same list with just one line of code.
squares = [value**2 for value in range(1, 11)]
print(squares)