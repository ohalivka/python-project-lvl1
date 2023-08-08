import random
import prompt
from brain_games.scripts.brain_games import greet


ROUNDS = 3
START_RANGE = 1
STOP_RANGE = 100


def calculate_result(number_one, number_two, operator):
	if operator == '+':
		result = number_one + number_two
	if operator == '-':
		result = number_one - number_two
	if operator == '*':
		result = number_one * number_two

	return result


def game():
	print('What is the result of the expression?')

	for r in range(ROUNDS):
		number_one = random.randint(START_RANGE, STOP_RANGE)
		number_two = random.randint(START_RANGE, STOP_RANGE)
		operator = random.choice(['+', '-', '*'])
		print(f'Question: {number_one} {operator} {number_two}')
		answer = prompt.integer('Your answer: ')
		result = calculate_result(number_one, number_two, operator)

		if result == answer:
			print('Correct!')
		else:
			print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'. Let's try again, Alina!")
			break
	else:
		print(f'Congratulations, Alina!')


def main():
	greet()
	game()


if __name__ == '__main__':
	main()
