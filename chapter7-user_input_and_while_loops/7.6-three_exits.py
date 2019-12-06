# conditinal test case for 7-4
topping = ''
while topping != 'quit':
    message = 'Please enter the toppping you like: '
    message += '\nEnter "quit" to end. '
    topping = input(message)
    if topping != 'quit':
        print(f'Adding {topping} to your pizza!\n')
