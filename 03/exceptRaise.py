# 意図的に例外を送出
raise ValueError('不正な引数です')

def get_book(index):
	items = ['note', 'notebook', 'sketchbook']
	try:
		return items[index]
	except IndexError as e:
		print('IndexErrorが発生しました')
		raise

get_book(3)
