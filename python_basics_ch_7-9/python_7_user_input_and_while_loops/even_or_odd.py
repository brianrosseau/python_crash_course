# Use the modulo operator % to determine if a number is even or odd.
# The modulo operator % gives the remainder when two numbers are divided.

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")