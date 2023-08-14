import random
import math


START_RANGE = 1
STOP_RANGE = 100
RULES = 'Find the greatest common divisor of given numbers.'


def start_game():
	# генерируем случайные числа
	number_one = random.randint(START_RANGE, STOP_RANGE)
	number_two = random.randint(START_RANGE, STOP_RANGE)

	# формируем маску для вопроса игроку
	question_options = f'{number_one} {number_two}'

	# вычисляем правильный ответ
	correct_answer = math.gcd(number_one, number_two)

	return str(correct_answer), question_options
