person_1 = {
    'name': 'Esther',
    'age': 21,
    'city': 'Perth',
    'mood': 'Happy',
    }
person_2 = {
    'name': 'Will',
    'age': 39,
    'city': 'Beijing',
    'mood': 'Relaxed',
    }
person_3 = {
    'name': 'Elka',
    'age': 26,
    'city': 'Perth',
    'mood': 'Excited',
}

people = [person_1, person_2, person_3]

for person in people:
    print(person['name'])
    print(person['age'])
    print(person['city'])
    print(person['mood'])