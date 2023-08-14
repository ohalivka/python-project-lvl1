from brain_games import engine
from brain_games.games import brain_even_logic


def main():
	engine.game(brain_even_logic.tell_the_rules(), brain_even_logic.game())


if __name__ == '__main__':
	main()
