sandwich_orders = ['chicken', 'beef', 'tuna', 'pork']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich.')
    finished_sandwiches.append(sandwich)

print('\nI have made these sandwiches: ')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
