buffet = ('meat', 'salad', 'bread', 'dessert', 'sides')

print("The buffet offers:")
for food in buffet:
    print(food)

# Cannot modify items in a tuple, because tuples cannot be changed.
buffet[2] = 'rocks'

#but we can redefine the variable to create a new tuple in its place.
buffet = ('meat', 'salad', 'bread', 'fruit', 'smashed potatoes')

print("The buffet changed its menu to:")
for food in buffet:
    print(food)



    

