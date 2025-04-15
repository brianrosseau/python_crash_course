def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['make'] = manufacturer
    car_info['model'] = model
    return car_info