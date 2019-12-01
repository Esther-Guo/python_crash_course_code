pizzas = ['Hawaii', 'BBQ', 'Bacon']

friend_pizzas = pizzas[:]

pizzas.append('Beef')

friend_pizzas.append('Chicken')

print('My favorate pizzas are: ')
for pizza in pizzas:
    print(pizza)

print('My friend’s favorite pizzas are: ')
for pizza in friend_pizzas:
    print(pizza)