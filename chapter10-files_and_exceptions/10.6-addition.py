print('enter p to exit.')

while True:
    first_num = input('Enter the first number to add: ')
    if first_num == 'q':
        break
    second_num = input('Enter the second number to add: ')
    if second_num == 'q':
        break
    try:
        sum = int(first_num) + int(second_num)
    except ValueError:
        print('At least one number you entered is not numerical.')
    else:
        print(f'The sum is {sum}.')
