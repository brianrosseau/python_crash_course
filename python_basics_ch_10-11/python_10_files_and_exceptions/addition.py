# Write a program that prompts for two numbers to add together and prints
#   a message that avoids a ValueError if someone types a letter.
print("Give me two numbers and I'll add them together.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You may only enter numbers.")
    else:
        print(answer)


'''
def addition(self, first_number, second_number):
    """Takes in two numbers and adds them together."""
    number_1 = input()
    '''