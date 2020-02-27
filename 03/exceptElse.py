def get_book_upper(index):
	items = ['note', 'notebook', 'sketchbook']
	try:
		book = str(items[index])
		return book.upper()
	except (IndexError, TypeError) as e:
		print(f'例外が発生しました: {e}')


get_book_upper(3)
get_book_upper('3')
