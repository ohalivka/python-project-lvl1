import prompt

ROUNDS = 3


def play_game(game):
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.RULES)

    for r in range(ROUNDS):
        correct_result, question_options = game.start_game()

        print(f'Question: {question_options}')

        player_response = input('Your answer: ')

        if correct_result == player_response:
            print('Correct!')
        else:
            print(f"'{player_response}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_result}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
