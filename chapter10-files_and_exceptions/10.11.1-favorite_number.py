import json

num = input('What is your favorite number? ')
filename = 'favorite_num.txt'

with open(filename, 'w') as f:
    json.dump(num, f)
