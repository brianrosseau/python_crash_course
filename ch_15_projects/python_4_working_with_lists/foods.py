my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # Important to use a slice. The [:] means we slice the entire list. In doing this we are assigning a copy, rather than making them equal.(see below)

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


#Correct code...
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]   

my_foods.append('cannoli')               # Here we append a different food to each respective list
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


#Incorrect code...
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods              #If we just make them equal without addding the slice, then when we append the lists, both lists look the same, wih both appended items.

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


# More loops exercise (4-12): Here we will use for loops to print both lists...
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]   

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)