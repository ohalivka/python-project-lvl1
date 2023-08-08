import random
import prompt
from brain_games.scripts.brain_games import greet


ROUNDS = 3
START_RANGE = 1
STOP_RANGE = 100


# проверяем число на четность
def is_even(num):
	if num % 2 == 0:
		res = 'yes'
	else:
		res = 'no'
	return res


def game():
	# рассказываем правила игры
	print('Answer "yes" if the number is even, otherwise answer "no".')

	# играем с пользователем
	for r in range(ROUNDS):
		# генерирум случайное число
		number = random.randint(START_RANGE, STOP_RANGE)

		# узнаем у пользователя ответ
		print(f'Question: {number}')
		answer = prompt.string('Your answer: ')

		# узнаем правильный ответ
		result = is_even(number)

		# сверяем ответ пользователя с правильным ответом
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
