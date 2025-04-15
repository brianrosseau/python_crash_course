rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yangtze': 'china'}

#This prints a sentence for each key-value pair that includes the key and value
for river, country in rivers.items():
    print(f"The {river.title()} River runs through {country.title()}.")

#This prints each key
for river in rivers.keys():
    print(river.title())

#Since the keys() method is default, it works the same to omit keys()...
for river in rivers:
    print(river.title())

#This prints each value
for country in rivers.values():
    print(country.title())