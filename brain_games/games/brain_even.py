import random


START_RANGE = 1
STOP_RANGE = 100
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def start_game():
    num = random.randint(START_RANGE, STOP_RANGE)

    if is_even(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return correct_answer, num
