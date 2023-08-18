import random


START_RANGE = 1
STOP_RANGE = 100
RULES = 'What is the result of the expression?'


def calculate_correct_answer(number_one, number_two, operator):
    match operator:
        case '+':
            return number_one + number_two
        case '-':
            return number_one - number_two
        case '*':
            return number_one * number_two


def start_game():
    number_one = random.randint(START_RANGE, STOP_RANGE)
    number_two = random.randint(START_RANGE, STOP_RANGE)
    operator = random.choice(['+', '-', '*'])

    correct_answer = calculate_correct_answer(number_one, number_two, operator)

    question_options = f'{number_one} {operator} {number_two}'

    return str(correct_answer), question_options
