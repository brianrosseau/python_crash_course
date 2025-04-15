#CHECKING FOR EQULITY
cars = ['audi', 'bmw', 'subaru', ' toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
car == 'bmw'

#Single quote is statement: set car equal to audi
car = 'audi'
#Double quote is question: is car equal to bmw?
car == 'bmw'

#in Python, checking for equality is case-sensitive
car = 'Audi'
car == 'audi'

car = 'Audi'
car.lower() == 'audi'

# the lower() method does not affect the original value of car
car

