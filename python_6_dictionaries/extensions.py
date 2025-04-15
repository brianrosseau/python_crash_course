rivers = {
    'nile': {
        'country': 'egypt',
        'length (miles)': 4132, 
        'drainage area (sq km)': 3254555,
        },
    'amazon': {
        'country': 'brazil', 
        'length (miles)': 4000,
        'drainage area (sq km)': 7000000,
        },
    'yangtze': {
        'country': 'china',
        'length (miles)': 3915,
        'drainage area (sq km)': 1800000,
        },
    'mississippi': {
        'country': 'usa',
        'length (miles)': 3710,
        'drainage area (sq km)': 2980000,
        },
    }

for river, information in rivers.items():
    print(f"\n{river.title()}")
    
    for info, stats in information.items():
        if info == 'country':
            if stats == 'usa':
                stats = stats.upper()
            else:
                stats = stats.title()
        if info == 'drainage area (sq km)':
            print(f"\t{info.capitalize()}:\t{stats}")
        else:
            print(f"\t{info.capitalize()}:\t\t{stats}")


#This prints the same info but puts the rivers in alphabelical order...
for river, information in sorted(rivers.items()):         # sorted () function
    print(f"\n{river.title()}")
    
    for info, stats in information.items():
        if info == 'country':
            if stats == 'usa':
                stats = stats.upper()
            else:
                stats = stats.title()
        if info == 'drainage area (sq km)':
            print(f"\t{info.capitalize()}:\t{stats}")
        else:
            print(f"\t{info.capitalize()}:\t\t{stats}")


##print out rivers in order of length and again in order of drainage area

