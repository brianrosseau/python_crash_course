cities = {
    'venice': {
        'country': 'italy', 
        'population': "257,777", 
        'fun fact': 'Venice is built on a group of 126 islands that are separated by expanses of open water and by canals; portions of the city are linked by 472 bridges.'
        },
    'hong kong': {
        'country': 'china',
        'population': "7,531,800",
        'fun fact': 'Hong Kong is one of the most densely populated countries in the world, and has a population density of 17,311 people per square mile.'
        },
    "macon, georgia": {
        'country': 'usa',
        'population': "156,337",
        'fun fact': "Macon is the allergy capital of the South, according to this author's unbiased opinion."
        },
    }

for city, information in cities.items():
    print(f"\n{city.title()}")

    for key, info in information.items():
        if key == 'country':
            if info == 'usa':
                info = info.upper()
            else:
               info = info.title()
        print(f"\t{key.capitalize()}:\t{info}")