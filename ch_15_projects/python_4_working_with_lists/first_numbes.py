for value in range(1,5):
    print(value)
#Notice "5" does not print, just 1 through 4.

for value in range(1, 6):
    print(value)
    #this prints 1 through 5.

for value in range(6):
    print(value)
# this prints 0 through 5.

numbers = list(range(1,6))
print(numbers)
# this prints a list of number, 1 through 5.

even_numbers = list(range(2, 11, 2))
print(even_numbers)
#this prints even numbers between 2 and 10. The third argument is a step size when generating numbers.

third_numbers = list(range(0, 217, 3))
print(third_numbers)
# prints a list of every third number, 0 through 216.

# the following code puts the first ten square numbers into a list.
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

# a more concise code would be...
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

#Simple statistics with a list of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
min(digits)
max(digits)
sum(digits)


num_list = list(range(111))
print(num_list)
min(num_list)
max(num_list)
sum(num_list)

