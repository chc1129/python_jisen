def has_book(items):
	for item in items:
		if 'book' in item:
			print('Found')
			break # ループを抜ける
	else:
		print('Not found')

has_book(['note'])

has_book(['note', 'notebook'])
