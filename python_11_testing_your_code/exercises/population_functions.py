# Here I simply modified the get_city_country() function from city_functions.py to include population

def get_city_country(city, country, population=''):
    """Generate a neatly formatted 'City, Country - population xxx' name."""
    if population:
        city_country = f"{city}, {country} - population {population}"
    else:
        city_country = f"{city}, {country}"
    return city_country.title()