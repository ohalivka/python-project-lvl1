import random


START_RANGE = 1
STOP_RANGE = 100
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


# проверяем число на четность
def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def start_game():
    # генерирум случайное число
    number = random.randint(START_RANGE, STOP_RANGE)

    # узнаем правильный ответ
    correct_answer = is_even(number)

    return correct_answer, number
