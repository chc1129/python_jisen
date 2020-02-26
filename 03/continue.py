def list_books(items):
	for item in items:
		if 'book' not in item:
			# 以降の処理をスキップして次のループに移る
			continue
		print(item)

list_books(['note', 'notebook', 'sketchbook'])
