import random


def random_dice():
    dice_first = random.randint(1, 6)
    dice_second = random.randint(1, 6)
    return dice_first, dice_second


(i, j) = random_dice()
print(f'({i}, {j})')
