import random

NUMBER_ROW_LIMIT = 6
LOWER_LIMIT = 1
UPPER_LIMIT = 45

number_generation = int(input("How many quick picks? "))

for i in range(number_generation):
    quick_pick = []
    while len(quick_pick) < NUMBER_ROW_LIMIT:
        num = random.randint(LOWER_LIMIT, UPPER_LIMIT)
        if num not in quick_pick:
            quick_pick.append(num)
    quick_pick.sort()
    print(" ".join(f"{n:2}" for n in quick_pick))