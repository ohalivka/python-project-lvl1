import random


START_RANGE = 1
STOP_RANGE = 100
RULES = 'What is the result of the expression?'


# вычисляем правильный ответ
def calculate_correct_answer(number_one, number_two, operator):
	match operator:
		case '+':
			return number_one + number_two
		case '-':
			return number_one - number_two
		case '*':
			return number_one * number_two


def start_game():
	# определяем операнды и оператор
	number_one = random.randint(START_RANGE, STOP_RANGE)
	number_two = random.randint(START_RANGE, STOP_RANGE)
	operator = random.choice(['+', '-', '*'])

	# вычисляем правильный ответ
	correct_answer = calculate_correct_answer(number_one, number_two, operator)

	# создаем пример для вопроса игроку
	question_options = f'{number_one} {operator} {number_two}'

	return str(correct_answer), question_options
