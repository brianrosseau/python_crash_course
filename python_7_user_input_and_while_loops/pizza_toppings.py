pizza_welcome = "Aarf! Welcome, to Able's Pizzaria!"
pizza_toppings = "\nWhat toppings would you like on your pizza? "
pizza_toppings += "\nPress 'enter' after each topping. Type 'quit' when done. "

print(pizza_welcome)

topping = ""
while topping != 'quit':
    topping = input(pizza_toppings)

    if topping != 'quit':
        print(f"\nAble will add {topping} to your pizza!")

