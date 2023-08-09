import random
import prompt
import math
from brain_games.scripts.brain_games import greet


ROUNDS = 3
START_RANGE = 1
STOP_RANGE = 100


def game():
	print('Find the greatest common divisor of given numbers.')

	for r in range(ROUNDS):
		number_one = random.randint(START_RANGE, STOP_RANGE)
		number_two = random.randint(START_RANGE, STOP_RANGE)

		print(f'Question: {number_one} {number_two}')
		answer = prompt.integer('Your answer: ')
		result = math.gcd(number_one, number_two)

		if answer == result:
			print('Correct!')
		else:
			print(f"{answer} is wrong answer ;(. Correct answer was {result}. Let's try again, Alina!")
			break
	else:
		print(f'Congratulations, Alina!')


def main():
	greet()
	game()


if __name__ == '__main__':
	main()
