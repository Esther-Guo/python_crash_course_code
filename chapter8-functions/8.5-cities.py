def describe_city(city, country='China'):
    """describe a city"""
    print(f'{city.title()} is in {country.title()}.')


describe_city('Beijing')
describe_city(city='shanghai')
describe_city('perth', 'Australia')