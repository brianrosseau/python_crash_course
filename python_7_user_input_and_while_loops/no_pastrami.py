sandwich_orders = ['pastrami', 'roast beef on rye', 'salmon salad surprise', 'pastrami', 'the works', 
                   'peanut butter grilled cheese', 'pastrami', 'pbj']

finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop(0)

    print(f"\nI made your {current_order} sandwich!")
    finished_sandwiches.append(current_order)

print("\nHere are all the sandwiches I made: ")
for sandwich in finished_sandwiches:
    if sandwich == 'pbj':
        sandwich = sandwich.upper()
    else:
        sandwich = sandwich.title()
    print(sandwich)