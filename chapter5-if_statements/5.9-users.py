# usernames = ['admin', 'esther', 'a', 'b', 'c']
usernames = []
user = 'a'

if usernames:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {user}, thank you for logging in again.')
else:
    print('We need to find some users!')