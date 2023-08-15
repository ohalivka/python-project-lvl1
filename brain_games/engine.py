import prompt

# количество раундов
ROUNDS = 3


def play_game(game):
	# приветствие
	print('Welcome to the Brain Games!')

	# узнаем имя
	name = prompt.string('May I have your name? ')
	print(f'Hello, {name}!')

	# рассказываем правила игры
	print(game.RULES)

	# играем в игру
	for r in range(ROUNDS):
		# узнаем правильный ответ
		correct_result, question_options = game.start_game()

		# задаем вопрос
		print(f'Question: {question_options}')

		# узнаем ответ пользователя
		player_response = input('Your answer: ')

		# сравниваем правильный ответ с ответом игрока и показываем результат
		if correct_result == player_response:
			print('Correct!')
		else:
			# игрок проиграл
			print(f"'{player_response}' is wrong answer ;(.")
			print(f"Correct answer was '{correct_result}'. Let's try again, {name}!")
			break
	else:
		# игрок выиграл
		print(f'Congratulations, {name}!')
