favorite_places = {
    'brian': ['church', 'home', 'anywhere with Lorie'], 
    'lorie': ['home', 'arrowhead', 'claystone'], 
    'able': ['the car', 'the hiking trail', "the neighbor's mailbox"],
    }

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place}")
