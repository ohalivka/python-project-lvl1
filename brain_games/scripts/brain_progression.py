import random
import prompt
from brain_games.scripts.brain_games import greet

ROUNDS = 3
SEQUENCE_NUMBERS = 10
START_RANGE = 1
STOP_RANGE = 100


def game():
	print('What number is missing in the progression?')

	for t in range(ROUNDS):
		fist_number = random.randint(START_RANGE, STOP_RANGE)
		step = random.randint(1, 10)
		sequence = [fist_number, ]
		for x in range(SEQUENCE_NUMBERS - 1):
			sequence.append(fist_number + step)
			fist_number += step

		index = random.randint(0, 9)
		result = sequence[index]
		sequence[index] = '..'
		f = list(map(str, sequence))

		print(f"Question: {' '.join(list(map(str, sequence)))}")
		answer = prompt.integer('Your answer: ')

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
