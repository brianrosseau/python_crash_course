# Exercise 9-13 Dice
from random import randint

class Die:
    """Represents a 6-sided rolling die."""

    def __init__(self, sides=6):
        """Initialize the die, setting the default number of sides to 6."""
        self.sides = sides

    def roll_die(self):
        """Prints a random number between (and including) 1 and the number of sides on the die."""
        roll = randint(1, self.sides)
        return roll

# Can do each roll individually...
print(Die().roll_die())

roll_1 = Die()
print(roll_1.roll_die())

roll_2 = Die()
print(roll_2.roll_die())

roll_3 = Die()
print(roll_3.roll_die())

# or let a loop do it for you...
# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
for toss_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("Results of 10 rolls of 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(10)       # override default, change sides to 10 (can also write it 'sides=10')

results = []
for toss_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("Results of 10 rolls of 10-sided die.")
print(results)

# Make a 20-sided die, and show the results of 20 rolls.
d20 = Die(sides=20)

results = []
for toss_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("Results of 10 rolls of 20-sided die.")
print(results)