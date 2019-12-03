current_users = ['admin', 'esther', 'will', 'jack', 'amy']
new_users = ['esther', 'will', 'a', 'b', 'c']

for new_user in new_users:
    if new_user in current_users:
        print(f'{new_user}:Please enter another username.')
    else:
        print(f'{new_user}:This username is available')
