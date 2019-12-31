import json

filename = 'favorite_num.txt'

with open(filename) as f:
    num = json.load(f)
    print(f'I know your favorite number is {num}.')
