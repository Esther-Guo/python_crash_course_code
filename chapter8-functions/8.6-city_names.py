def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f'{city.title()}, {country.title()}'


string = city_country('beijing', 'china')
print(string)
string = city_country('seattle', 'united states')
print(string)
string = city_country('perth', 'australia')
print(string)
