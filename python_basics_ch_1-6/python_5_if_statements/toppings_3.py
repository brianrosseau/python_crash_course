#CHECKING FOR SPECIAL ITEMS
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for topping in requested_toppings:
    print(f"Adding {topping}.")

print("\nFinished making your pizza!")

#but what if pizzaria runs out of green peppers?
for topping in requested_toppings:
    if topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {topping}.")

print("\nFinished making your pizza!")

#CHECKING THAT A LIST IS NOT EMPTY
requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
#When the name of a list appears in an if statement, Python returns True if 
#the list contains at least one item; an empty list evaluates to False.
#Since it was an empty list (and thus the if statement evaluated to False),
#the else statement was executed instead.

requested_toppings = ['green peppers', 'pepperoni']

if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
#Since in this example there was something in the list, the if statement
#evaluated to True, and therefore the if statement was executed.


#USING MULTIPLE LISTS
available_toppings = ['mushrooms', 'olives', 'greeen peppers', 'pepperoni',
                      'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping} to your pizza.")
    else:
        print(f"Sorry we don't have {topping}.")

print("\nFinished making your pizza!")


#Here, each item in requested_toppings is checked against the list of
#available toppings before it's added to the pizza.