number = input("\nGive me a number and I will tell you if it is a multiple of 10: ")
number = int(number)

if number %10 == 0:
    print(f"Yes, {number} is a multiple of 10!")
else:
    print(f"Sorry, {number} is not a multipe of 10.")