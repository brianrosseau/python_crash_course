sandwich_orders = ['roast beef on rye', 'salmon salad surprise', 'the works', 
                   'peanut butter grilled cheese', 'pbj']

finished_sandwiches = []

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