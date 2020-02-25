def first_item(items):
	if items: # 空のコンテナオブジェクトは偽になる
		return print(items[0])
	else:
		return None

first_item(['book'])

first_item([]) # Noneの場合は何も表示されない
