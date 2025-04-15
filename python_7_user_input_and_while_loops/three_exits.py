pizza_welcome = "\nAarf! Welcome, to Able's Pizzaria!"
pizza_toppings = "\nWhat toppings would you like on your pizza? "
pizza_toppings += "\nPress 'enter' after each topping. Type 'quit' when done. "

print(pizza_welcome)

active = True
while active:
    topping = input(pizza_toppings)

    if topping == 'quit':
        active = False
        print("\nAble will have your pizza ready in ruff-ly five minutes. Aarf!")
        break
    else:
        print(f"\nAble will add {topping} to your pizza!")



