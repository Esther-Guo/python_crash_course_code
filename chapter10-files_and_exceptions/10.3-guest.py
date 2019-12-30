filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(input('What is your name? '))
    print('Hi, I already add your name in the file.')