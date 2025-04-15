from city_functions import get_city_country

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nEnter the name of a city: ")
    if city == 'q':
        break
    country = input("\nEnter the country in which that city is located: ")
    if country == 'q':
        break

    formatted_city_country = get_city_country(city, country)
    print(f"\tThe location you entered is: {formatted_city_country}")