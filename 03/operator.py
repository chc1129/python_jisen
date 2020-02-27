import random

def lottery(goods):
# itemsへの代入が行われる
	if item := random.choice(goods):
		return print(item)
	else:
		return print('MISS!!')

books = ['notebook', 'sketchbook', None, None, None]

lottery(books)
