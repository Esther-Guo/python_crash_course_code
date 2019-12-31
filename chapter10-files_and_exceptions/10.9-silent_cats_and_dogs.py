files = ['cats.txt', 'dogs.txt']

for f in files:
    try:
        with open(f) as f_object:
            content = f_object.read()
    except FileNotFoundError:
        pass
    else:
        print(f'Reading file: {f}')
        print(content)
