import random


START_RANGE = 1
STOP_RANGE = 100


# рассказываем правила игроку
def tell_the_rules():
	return 'Answer "yes" if the number is even, otherwise answer "no".'


# проверяем число на четность
def is_even(num):
	if num % 2 == 0:
		return 'yes'
	else:
		return 'no'


def game():
	# генерирум случайное число
	number = random.randint(START_RANGE, STOP_RANGE)

	# узнаем правильный ответ
	result = is_even(number)

	print (result, number)
