def make_shirt(size, message):
    """make a shirt of particular size with message"""
    print(f'The size of shirt is {size.upper()}.')
    print(f'The message on the shirt is {message}.')


make_shirt('s', 'Merry Chrismas')
make_shirt(size='s', message='Merry Chrismas')
