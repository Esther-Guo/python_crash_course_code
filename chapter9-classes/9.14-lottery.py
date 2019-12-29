from random import choice

lottery = ['A', 'E', 'F', 'W', 'M', 12, 90, 28, 39, 10, 22, 45, 77, 98, 37]
final = []

while len(final) < 4:
    chosen = choice(lottery)
    if chosen not in final:
        final.append(chosen)

print(final)
