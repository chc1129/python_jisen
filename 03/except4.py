def get_book_wrapper(index):
	try:
		# IndexErrrはそのまま送出されてくる
		return get_book(index)
	except IndexError:
		print(f'IndexErrorが発生しました')
		return print('範囲外です')

get_book_wrapper(3)
