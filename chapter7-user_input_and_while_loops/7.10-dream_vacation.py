active = True
polling = {}
prompt = 'If you could visit one place in the world,'
prompt += '\nwhere would you go? '

while active:
    name = input('What is your name? ')
    place = input(prompt)
    polling[name] = place

    response = input('Would you like the polling to continue?(y/n) ')
    if response == 'n':
        active = False

for name, place in polling.items():
    print(f'{name.title()} wants to visit {place.title()}.')