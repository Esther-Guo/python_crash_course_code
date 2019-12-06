active = True
while active:
    message = 'Please enter the toppping you like: '
    message += '\nEnter "quit" to end. '
    topping = input(message)
    if topping == 'quit':
        active = False
    else:
        print(f'Adding {topping} to your pizza!\n')
