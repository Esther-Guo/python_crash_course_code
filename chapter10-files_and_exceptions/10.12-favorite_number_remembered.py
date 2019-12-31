import json

filename = 'favorite_num.txt'

try:
    with open(filename) as f:
        num = json.load(f)
except FileNotFoundError:
    num = input('What is your favorite number? ')
    with open(filename, 'w') as f:
        json.dump(num, f)
    print('I have keep your favorite number.')
else:
    print(f'I know your favorite number is {num}.')
