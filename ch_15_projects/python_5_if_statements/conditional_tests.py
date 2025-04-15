car = 'subaru'
print("Is car ==  'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')


dog = 'Able'
print("Is dog == 'Able'? I predict True.")
print(dog == 'Able')

print("Is dog == 'able'? I predict False.")
print(dog == 'able')

print("Is dog.lower() == 'able'? I predict True.")
print(dog.lower() == 'able')

wife = ['lovely', ' beautiful', 'encouraging', 'gift from God', 'super-hot', 'best friend', 'sweet']

print("Is wife sweet? I predict True")
print('sweet' in wife)

print("Is wife boring? I predict False.")
print('boring' in wife)

age = 46
print("Is age > 35? I predict True.")
print(age > 35)

print("Is age >= 55? I predict False.")
print(age >= 55)

stooges = ['larry', 'curly', 'moe']
print("Is 'larry' not in stooges? I predict False.")
print('larry' not in stooges)

print("Is 'Moe' not in stooges? I predict True.")
print('Moe' not in stooges)

print("Is 'moe' not in stooges? I predict False.")
print('moe' not in stooges)

#MORE CONDITIONAL TESTS

color = ['green']
if c not in color:
    print(f"c.title() is not the right color")

print("Is 'blue' in color? I predict False.")
print('blue' in color)

print("Is 'green' in color? I predict True.")
print('green' in color)

name = 'George'
print("Is name == 'george'? I predict False.")
print(name == 'george')

print("Is name.lower() == 'george'? I predict True.")
print(name.lower() == 'george')

number_0 = 255
number_1 = 355
print("Is number_0 > 300 and number_1 > 300? I predict False.")
print(number_0 > 300 and number_1 > 300)

print("Is number_0 > 300 or number_1 > 300? I predict True.")
print(number_0 > 300 or number_1 > 300)

