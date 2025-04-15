motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Modifying elements in a list
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding elements to a list
# 1. Appending means adding a new element to the end of a list. Use the append() method.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
print(motorcycles)
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#2. Insert elements into your list at any position using the insert() method.
motorcycles.insert(0,'ducati')
print(motorcycles)
motorcycles.insert(2, 'tricycle')
print(motorcycles)

# Removing Elements from a List
#1. del statement. Remove an item using the del statement if you know the position of the item you want to remove.
del motorcycles[2]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
del motorcycles[0]
print(motorcycles)
# you can no longer access the value that was removed when using the del statement.

#2. pop() method. Remove and item using the pop() method. The pop() method removes an item from a list, but it lets you work with that item after removing it.
motorcycles.insert(0, 'honda')
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(motorcycles)

motorcycles.append('suzuki')
print(motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
print(motorcycles)

#3. Popping items from any position in a list. Include the index of the item you want to remove.
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#4. remove() method. Removing an item by value. This is done if you don't know the index, but you know the value.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# like the pop() method, the remove() method allows you to work with the item that was removed.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

