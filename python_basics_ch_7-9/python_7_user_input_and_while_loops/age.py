# This prints an error because the age that is entered is a string, and 
# Python cannot compare a string to numerical value
'''
age = input("How old are you? ")
print(age)
print(age >= 18)
'''

# But using the int() function converts the age string to an integer
age = input("How old are you? ")
age = int(age)
print(age >= 18)