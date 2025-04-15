from population_functions import get_city_country

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nEnter the name of a city: ")
    if city == 'q':
        break
    country = input("\nEnter the country in which that city is located: ")
    if country == 'q':
        break
    population = input("\nEnter that city's population, or enter 'u' if unknown: ")
    if population == 'q':
        break
    if population == 'u':
        population = 'unknown'

    formatted_city_country_population = get_city_country(city, country, population)
    print(f"\tThe location you entered is: {formatted_city_country_population}")