rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')

print('Rivers included: ')
for river in rivers.keys():
    print(river)

print('\nCountries included: ')
for country in rivers.values():
    print(country)