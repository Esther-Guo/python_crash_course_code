guest_list = ['Mike','Sonnam','Ham']

guest_list.insert(0, 'Amy')
guest_list.insert(2, 'Larren')
guest_list.append('Esther')

print(f'Can I invite you for dinner, {guest_list[0]}?')
print(f'Can I invite you for dinner, {guest_list[1]}?')
print(f'Can I invite you for dinner, {guest_list[2]}?')
print(f'Can I invite you for dinner, {guest_list[3]}?')
print(f'Can I invite you for dinner, {guest_list[4]}?')
print(f'Can I invite you for dinner, {guest_list[5]}?')

print(f'I can only invite 2 people now.')

guest = guest_list.pop()
print(f'Sorry I cannot have you for dinner, {guest}.')
guest = guest_list.pop()
print(f'Sorry I cannot have you for dinner, {guest}.')
guest = guest_list.pop()
print(f'Sorry I cannot have you for dinner, {guest}.')
guest = guest_list.pop()
print(f'Sorry I cannot have you for dinner, {guest}.')

print(f'You can still come for dinner, {guest_list[0]}.')
print(f'You can still come for dinner, {guest_list[1]}.')

del guest_list[0]
del guest_list[0] # only one left!!!!

print(guest_list)