import random


SEQUENCE_NUMBERS = 9
START_RANGE = 1
STOP_RANGE = 100
RULES = 'What number is missing in the progression?'


def start_game():
	# генерируем рандомное число, с которого будет начинаться последовательность
	fist_number = random.randint(START_RANGE, STOP_RANGE)

	# генерируем шаг последовательности
	step = random.randint(0, 10)

	# создаем список
	sequence = [fist_number, ]

	# наполняем список
	for _ in range(SEQUENCE_NUMBERS):
		sequence.append(fist_number + step)
		fist_number += step

	# определяем индекс числа, которое скроем
	hidden_number_index = random.randint(0, 9)

	# сохраняем число и заменяем его точками
	correct_answer = sequence[hidden_number_index]
	sequence[hidden_number_index] = '..'

	# создаем маску для вопроса игроку
	question_options = f"{' '.join(list(map(str, sequence)))}"

	return str(correct_answer), question_options
