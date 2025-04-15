def describe_city(city, country='the USA'):
    """Names a city and the country in which it is located."""
    print(f"{city.title()} is in {country}.")

describe_city('New York')
describe_city('Atlanta')
describe_city('London', 'the UK')
