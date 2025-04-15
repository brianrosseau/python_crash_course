brian = {'first_name': 'brian', 'last_name': 'rosseau', 'age': 46,
         'city': 'macon, georgia'}

print(brian['city'].title())



lorie = {'first_name': 'lorie', 'last_name': 'rosseau', 'age': 38,
         'city': 'macon, georgia'}

angela = {'first_name': 'angela', 'last_name': 'rosseau', 'age': 44,
          'city': 'warner robins, georgia'}

people = [brian, lorie, angela]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name.title()} is {person['age']} years old and lives in {person['city'].title()}.")

