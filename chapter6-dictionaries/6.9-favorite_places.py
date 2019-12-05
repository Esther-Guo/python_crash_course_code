favorite_places = {
    'amy': ['Paris'],
    'brown': ['Bankok', 'Denpasar'],
    'charles': ['London', 'Beijing'],
}

for person, places in favorite_places.items():
    if len(places) == 1:
        print(f"{person.title()}'s favotire place is: ")
    else:
        print(f"{person.title()}'s favorite places are: ")
    for city in places:
        print(city)