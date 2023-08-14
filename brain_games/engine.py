import prompt as prompt


ROUNDS = 3


def game(rules, generate):
	# приветствие
	print('Welcome to the Brain Games!')

	# узнаем имя
	name = prompt.string('May I have your name? ')
	print(f'Hello, {name}!')

	# рассказываем правила игры
	print(rules)

	# играем в игру
	for r in range(ROUNDS):
		# узнаем правильный ответ
		result, question_options = generate

		# задаем вопрос
		print(f'Question: {question_options}')

		# узнаем ответ пользователя
		answer = input('Your answer: ')

		# сравниваем правильный ответ с ответом игрока и показываем результат
		if result == answer:
			print('Correct!')
		else:
			print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'. Let's try again, {name}!")
			break
	else:
		print(f'Congratulations, {name}!')


def main():
	game()


if __name__ == '__main__':
	main()
