while True:
    age = input('Please input your age:\nEnter "quit" when you are finished. ')

    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        fee = 0
    elif age < 12:
        fee = 10
    else:
        fee = 15
    print(f'The cost of your ticket is ${fee}.\n')
