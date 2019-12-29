from random import choice

lottery = ['A', 'E', 'W', 'M', 28, 98, 37, 24, 90, 99]

my_ticket = ['E', 37, 28, 98]
same = False
count = 1


def poll_lottery(lottery):
    chosen_lottery = []
    while len(chosen_lottery) < 4:
        chosen = choice(lottery)
        if chosen not in chosen_lottery:
            chosen_lottery.append(chosen)
    return chosen_lottery


def compare(chosen, my_ticket):
    for item in chosen:
        if item not in my_ticket:
            return False
    return True


chosen = poll_lottery(lottery)
while not compare(chosen, my_ticket):
    chosen = poll_lottery(lottery)
    count += 1

print(count)
