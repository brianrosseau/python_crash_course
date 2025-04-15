# The test below fails because it does not include population.
'''
from population_functions import get_city_country

def test_city_country():
    """Do places like 'Santiago, Chile' work?"""
    formatted_city = get_city_country('santiago', 'chile')
    assert formatted_city == 'Santiago, Chile'
'''


# We will add population below and the test will pass.

from population_functions import get_city_country

def test_city_country_population():
    """Do places like 'Santiago, Chile' work?"""
    formatted_city = get_city_country('santiago', 'chile', '5000000')
    assert formatted_city == 'Santiago, Chile - Population 5000000'