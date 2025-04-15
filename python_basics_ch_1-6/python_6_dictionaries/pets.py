#Example of Dictionaries in a List

pet_1 = {'animal': 'dog', 'pet_name': 'able', 'owner_first_name': ['lorie', 'brian'],
         'owner_last_name': 'rosseau'}
pet_2 = {'animal': 'cat', 'pet_name': 'mitch', 'owner_first_name': ['steve', 'kathy'],
         'owner_last_name': 'wolfe'}
pet_3 = {'animal': 'dog', 'pet_name': 'flower', 'owner_first_name': ['mike', 'hideko'],
         'owner_last_name': 'jones'}
pet_4 = {'animal': 'moose', 'pet_name': 'bullwinkle', 'owner_first_name': ['rocky'],
         'owner_last_name': 'squirrel'}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    if len(pet['owner_first_name']) > 1:
        owner_full_name = f"{pet['owner_first_name'][0].title()} and {pet['owner_first_name'][1].title()} {pet['owner_last_name'].title()}"
    elif len(pet['owner_first_name']) == 1:
        owner_full_name = f"{pet['owner_first_name'][0].title()} {pet['owner_last_name'].title()}"
    print(f"{pet['pet_name'].title()} is a {pet['animal']} who belongs to {owner_full_name}.")


