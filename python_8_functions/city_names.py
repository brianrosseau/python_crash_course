def city_country(city, country):
    """Displays the name of a city and country"""
    full_location_name = f"{city.title()}, {country.title()}"
    return full_location_name

destination = city_country('paris', 'france')
print(destination)

destination = city_country('macon', 'georgia')
print(destination)

destination = city_country('venice', 'italy')
print(destination)

