def make_car(manufacturer, model_name, **car):
    """Make a dictionary representing a car."""
    car['manufacturer'] = manufacturer.title()
    car['model name'] = model_name.title()
    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
