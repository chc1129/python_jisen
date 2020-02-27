import random

def lottery(goods):
	item = random.choice(goods)
	if item:
		return print(item)
	else:
		return print('MISS!!')

books = ['notebook', 'sketchbook', None, None, None]

lottery(books)
