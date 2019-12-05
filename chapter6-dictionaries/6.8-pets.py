pet_1 = {
    'type': 'dog',
    'name': 'esther',
    }
pet_2 = {
    'type': 'cat',
    'name': 'amy',
    }
pet_3 = {
    'type': 'kangaroo',
    'name': 'jack',
    }

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f'{pet["name"].title()} owns a {pet["type"]}.')