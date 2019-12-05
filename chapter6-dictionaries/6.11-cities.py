cities = {
    'Beijing': {
        'country': 'China',
        'population': 21_542_000,
        'fact': "The world's third most populous city proper."
        },
    'London': {
        'country': 'China',
        'population': 8_908_081,
        'fact': "Stands on the River Thames in the south-east of England."
        },
    'Thimphu': {
        'country': 'Bhutan',
        'population': 114_551,
        'fact': "The capital and largest city of Bhutan."
        },
}

for city, city_info in cities.items():
    print(f"{city} is located in {city_info['country']}")
    print(f"{city} owns a popuation of {city_info['population']}")
    print(f"One fact about {city}: {city_info['fact']}\n")