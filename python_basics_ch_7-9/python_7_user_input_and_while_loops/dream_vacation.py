# Write a program that polls users about their dream vacation

# Start with an empty dictionary
responses = {}

# Set a flag to show that polling is active
polling_active = True

while polling_active:
    # Prompt people to give their name and dream vacation destination
    name = input("What is your name? ")
    destination = input("If you could visit one place in the world, where would you go? ")

    # Add responses to the dictionary
    responses[name] = destination

    # Ask if anyone else would like to take the poll
    repeat = input("Would you like to let someone else respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
# Print results of poll
print("\n--- Poll Results ---")
for name, destination in responses.items():

    print(f"{name.title()} would like to visit {destination.title()}.")