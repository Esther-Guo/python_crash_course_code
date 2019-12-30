filename = 'responses.txt'

responses = []
while True:
    response = input('Why do you like programming? ')
    responses.append(response)
    ctn = input('Would you like someone else to respond?(y/n) ')
    if ctn == 'n':
        break

with open(filename, 'w') as f:
    for response in responses:
        f.write(f'{response}\n')         