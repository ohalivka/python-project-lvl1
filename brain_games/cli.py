import prompt


def welcome_user():
	name = prompt.string('May T have your name? ')
	print(f'Hello, {name}!')


def main():
	welcome_user()


if __name__ == '__main__':
	main()
