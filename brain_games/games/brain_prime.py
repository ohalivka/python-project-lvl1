import random


SEQUENCE_NUMBERS = 10
START_RANGE = 1
STOP_RANGE = 100
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# вычисляем правильный ответ
def is_prime(number):
    for n in range(2, int(number)):
        if number % n == 0:
            return 'no'
    else:
        return 'yes'


def start_game():
    # генерируем случайное число
    number = random.randint(START_RANGE, STOP_RANGE)

    # вычисляем правильный ответ
    correct_answer = is_prime(number)

    return correct_answer, number
