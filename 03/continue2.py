def list_books(items):
	copied = items.copy()
	while copied:
		# 先頭の要素を取り出す
		item = copied.pop(0)
		if 'book' not in item:
			# 以降の処理をスキップして次のループに移る
			continue
		print(item)

list_books(['note', 'notebook', 'sketchbook'])
