def first_item(items):
	if len(items) > 0: # 要素数から空かどうかを判定
		return print(items[0])
	else:
		return None

first_item(['book'])
first_item([]) # Noneの場合は何も表示されない
