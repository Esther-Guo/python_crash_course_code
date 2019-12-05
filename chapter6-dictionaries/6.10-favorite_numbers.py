favorite_numbers = {
    'Paul': [40, 90],
    'Eno': [31],
    'Lynn': [20, 0, 89],
    'Esther': [8, 54],
    'Vincent':[3],
    }

for person, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"{person}'s favorite number is: ")
    else:
        print(f"{person}'s favorite numbers are: ")
    for number in numbers:
        print(f"\t{number}")