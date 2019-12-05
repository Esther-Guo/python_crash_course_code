number = input('How many of you will be eating here: ')
number = int(number)

if number > 8:
    print('Please wait for a table.')
else:
    print('The table is ready.')