files = ['cats.txt', 'dogs.txt']

for f in files:
    try:
        with open(f) as f_object:
            content = f_object.read()
    except FileNotFoundError:
        print(f'{f} cannot be found in the working directory.')
    else:
        print(f'Reading file: {f}')
        print(content)
