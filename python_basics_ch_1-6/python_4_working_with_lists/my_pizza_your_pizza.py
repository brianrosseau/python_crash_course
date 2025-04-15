pizzas = ['pepperoni', 'supreme', 'meat-lovers', 'dairy-free']
friend_pizzas = pizzas[:]

pizzas.append('veggie-lovers')
friend_pizzas.append('cheese')

print("My favorite pizzas are:")
for pizza  in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

