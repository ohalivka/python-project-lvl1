import random


START_RANGE = 1
STOP_RANGE = 100
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def start_game():
    number = random.randint(START_RANGE, STOP_RANGE)

    correct_answer = is_even(number)

    return correct_answer, number
