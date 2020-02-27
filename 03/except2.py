def get_book(index):
	items = ['note', 'notebook', 'sketchbook']
	try:
		return items[index]
	except IndexError:
		print('IndexErrorが発生しました')
		return print('範囲外です')
	except TypeError:
		print('TypeErrorが発生しました')
		return print('範囲外です')

get_book(3)

get_book('3')
