import random
NUMBER_OF_RANDOM_NUMBERS = 6
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBERS = 45

number_of_quick_picks = int("How many quick picks: ")
for x in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBER_OF_RANDOM_NUMBERS):
            number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBERS)
            while number in quick_pick:
                number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBERS)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))