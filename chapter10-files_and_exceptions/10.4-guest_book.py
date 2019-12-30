filename = 'guest_book.txt'

with open(filename, 'a') as f:
    while True:
        name = input('What is your name?(q to quit) ')
        if name == 'q':
            break
        else:
            f.write(f'{name}\n')
