favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = ['jen', 'sarah', 'esther', 'will']

for person in people:
    if person not in favorite_languages.keys():
        print(f'{person.title()}, please tale the poll.')
    else:
        print(f'{person.title()}, thanks for taking the poll!')