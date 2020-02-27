def get_book(index):
	items = ['note', 'notebook', 'sketchbook']
	try:
		return print(items[index])
	except IndexError:
		return print('範囲外です')

get_book(10) # IndexErrorを適切に処理できている
