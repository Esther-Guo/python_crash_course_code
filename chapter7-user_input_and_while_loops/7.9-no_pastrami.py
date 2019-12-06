sandwich_orders = [
    'pastrami', 'chicken', 'beef', 'pastrami', 'pastrami', 'tuna', 'pork'
    ]

print('The deli has run out of pastrami!')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
