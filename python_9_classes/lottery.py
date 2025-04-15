# Exercise 9-4 and 9-5

# Exercise 9-4 Lottery

from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []
print("Let's see what the winning ticket is...")

# The winning ticket has 4 numbers or letters.
while len(winning_ticket) < 4:
    winning_num_let = choice(possibilities)

    # Only add the pulled item to the winning ticket if it hasn't already been pulled.
    if winning_num_let not in winning_ticket:
        print(f"We pulled a {winning_num_let}!")
        winning_ticket.append(winning_num_let)

print(f"The final winning ticket is: {winning_ticket}")
print("Any ticket matching these 4 letters or numbers wins a prize!")


# Exercise 9-5 Lottery Analysis

def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""

    # The winning ticket has 4 numbers or letters.
    while len(winning_ticket) < 4:
        winning_num_let = choice(possibilities)

        # Only add the pulled item to the winning ticket if it hasn't already been pulled.
        if winning_num_let not in winning_ticket:
            print(f"We pulled a {winning_num_let}!")
            winning_ticket.append(winning_num_let)

    return winning_ticket

def make_my_ticket(possibilites):
    """Return a random ticket from a set of possibilites."""

    my_ticket = []
    while len(my_ticket) < 4:
        num_let = choice(possibilites)

        # Only add the pulled item to my_ticket if it hasn't already been added.
        if num_let not in my_ticket:
            my_ticket.append(num_let)

    return my_ticket


def check_ticket(played_ticket, winning_ticket):
    # Check all elements in the played, ticket and return False if they are 
    # not in the winning ticket.
    for element in played_ticket:
        if element not in winning_ticket:
            return False
        
    return True


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)


plays = 0
won = False

while not won:
    new_ticket = make_my_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")