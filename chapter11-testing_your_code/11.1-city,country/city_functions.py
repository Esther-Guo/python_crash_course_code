def city_country(city, country, population=''):
    if population:
        formatted_name = f'{city.title()}, {country.title()}'
        formatted_name += f' - population {population}'
        return formatted_name
    else:
        formatted_name = f'{city}, {country}'
        return formatted_name.title()
