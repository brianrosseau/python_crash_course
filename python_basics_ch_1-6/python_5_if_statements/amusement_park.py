age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

#More efficent way of doing the same thing...(it is also easier to edit if needed)
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

#you can have as many elif statements as you want
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age >= 65:
    price = 20
else:
    price = 40

print(f"Your admission cost is ${price}.")

#or
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

#do not need to use an 'else' statment at the end
#can use an 'elif' in its place
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")

