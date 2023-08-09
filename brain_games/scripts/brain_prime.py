import random
import prompt
from brain_games.scripts.brain_games import greet


ROUNDS = 3
SEQUENCE_NUMBERS = 10
START_RANGE = 1
STOP_RANGE = 100


def is_prime(number):
	for x in range(2, int(number/2)):
		if number % x == 0:
			return 'no'
	else:
		return 'yes'


def game():
	print('Answer "yes" if given number is prime. Otherwise answer "no".')

	for x in range(ROUNDS):
		number = random.randint(START_RANGE, STOP_RANGE)
		result = is_prime(number)
		print(f"Question: {number}")
		answer = prompt.string('Your answer: ')

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
