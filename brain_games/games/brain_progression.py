import random


SEQUENCE_NUMBERS = 9
START_RANGE = 1
STOP_RANGE = 100
RULES = 'What number is missing in the progression?'


def start_game():
    fist_number = random.randint(START_RANGE, STOP_RANGE)

    step = random.randint(0, 10)

    sequence = [fist_number, ]

    for _ in range(SEQUENCE_NUMBERS):
        sequence.append(fist_number + step)
        fist_number += step

    hidden_number_index = random.randint(0, 9)

    correct_answer = sequence[hidden_number_index]
    sequence[hidden_number_index] = '..'

    question_options = f"{' '.join(list(map(str, sequence)))}"

    return str(correct_answer), question_options
