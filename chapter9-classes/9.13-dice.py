from random import randint


class Die:
    """Describe a dice"""
    def __init__(self, sides=6):
        """Initialize a dice"""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides"""
        num = randint(1, self.sides)
        return num


die1 = Die()
for i in range(10):
    print(die1.roll_die())

die2 = Die(10)
die3 = Die(20)
for i in range(10):
    print(f'first: {die2.roll_die()}')
    print(f'second: {die3.roll_die()}')
