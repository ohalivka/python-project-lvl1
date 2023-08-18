import random
import math


START_RANGE = 1
STOP_RANGE = 100
RULES = 'Find the greatest common divisor of given numbers.'


def start_game():
    number_one = random.randint(START_RANGE, STOP_RANGE)
    number_two = random.randint(START_RANGE, STOP_RANGE)

    question_options = f'{number_one} {number_two}'

    correct_answer = math.gcd(number_one, number_two)

    return str(correct_answer), question_options
