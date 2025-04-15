favorite_numbers = {
    'brian': [5, 11, 19],
    'lorie': [10, 25, 85],
    'able': [1, 1, 1, 1, 1, 1],
    'angela': [8],
    'rob': [11, 2013487504517, 4]
    }

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(f"\n{name.title()}'s favorite numbers are:")
    else:
        print(f"\n{name.title()}'s favorite number is:")
    
    for number in numbers:
        print(f"\t{number}")