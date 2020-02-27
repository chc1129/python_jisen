def get_book(index):
	items = ['note', 'notebook', 'sketchbook']
	try:
		return items[index]
	except TypeError: # IndexErrorは補足しない
		print(f'TypeErrorが発生しました')
		return print('範囲外です')

#get_book(3)
get_book('3')
