from city_functions import get_city_country

def test_city_country():
    """Do places like 'Santiago, Chile' work?"""
    formatted_city = get_city_country('santiago', 'chile')
    assert formatted_city == 'Santiago, Chile'