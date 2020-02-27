def get_book(index):
	items = ['note', 'notebook', 'sketchbook']
	try:
		return items[index]
	except (IndexError, TypeError) as e:
		print(f'例外が発生しました: {e}')
		return print('範囲外です')


# IndexErrorが発生している
get_book(3)

# TypeErrorが発生している
get_book('3')
