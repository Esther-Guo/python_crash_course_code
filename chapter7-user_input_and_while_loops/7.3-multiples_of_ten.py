num = input('Please input a number: ')
num = int(num)

if num % 10 == 0:
    print(f'{num} is divided by 10.')
else:
    print(f'{num} is not a multiple of 10.')